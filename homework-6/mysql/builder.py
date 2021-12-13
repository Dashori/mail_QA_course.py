from mysql.models import TotalCount, CountByType, TopMostFrequent
from mysql.models import TopBiggestClientError, TopFrequentServerError

class SQLBuilder:

    def __init__(self, client, path):
        self.client = client
        self.path = path
        self.requests = self.read_data()

    def read_data(self):
        with open(self.path) as file:
            requests = file.readlines()
            requests = [request.split() for request in requests]
            return requests

    def count_total(self):
        row = TotalCount(count=len(self.requests))
        self.client.session.add(row)
        self.client.session.commit()
        return row

    def count_by_type(self):
        dict = {}
        rows = []
        for request in self.requests:
            request_type = request[5][1:]
            if request_type in dict:
                dict[request_type] += 1
            elif len(request_type) < 7:
                dict[request_type] = 1
        
        for request_type, count in dict.items():
            row = CountByType(count=int(count), type_name=request_type)
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def top_10(self):
        dict = {}
        rows = []
        for request in self.requests:
            url = request[6]
            if url in dict:
                dict[url] += 1
            else:
                dict[url] = 1

        
        for url, count in sorted(dict.items(),
                                 key=lambda x: x[1],
                                 reverse=True)[:10]:
            row = TopMostFrequent(
                count=int(count),
                url=url)
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def top_4xx_requests(self):
        data = []
        rows = []
        for request in self.requests:
            ip = request[0]
            url = request[6]
            status = request[8]
            size = request[9]
            if status[0] == '4':
                item = (url, status, int(size), ip)
                data.append(item)

        for item in sorted(data,
                           key=lambda x: x[2],
                           reverse=True)[:5]:
            row = TopBiggestClientError(
                url=item[0],
                rc=int(item[1]),
                size=int(item[2]),
                ip=item[3])
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def top_5xx_users(self):
        dict = {} 
        rows = []
        for request in self.requests:
            ip = request[0]
            status = request[8]
            if status[0] == '5':
                if ip in dict:
                    dict[ip] += 1
                else:
                    dict[ip] = 1

        for ip, count in sorted(dict.items(),
                                key=lambda x: x[1],
                                reverse=True)[:5]:
            row = TopFrequentServerError(
                ip=ip,
                count=int(count))
            rows.append(row)
        self.client.session.bulk_save_objects(rows)
        self.client.session.commit()
        return rows

    def run_all(self):
        self.count_total()
        self.count_by_type()
        self.top_10()
        self.top_4xx_requests()
        self.top_5xx_users()