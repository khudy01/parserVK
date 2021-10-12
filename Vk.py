from Requests import Request

class VK:

    def getCount(self, domain, token):
        version = "5.131"
        count = 100
        offset = 0
        request = f"https://api.vk.com/method/wall.get" \
                  f"?access_token={token}" \
                  f"&v={version}" \
                  f"&domain={domain}" \
                  f"&count={count}" \
                  f"&offset={offset}"
        answer = Request(request)["response"]["count"]
        return answer

    def wallGet(self, domain, token, offset):
        version = "5.131"
        count = 100
        request = f"https://api.vk.com/method/wall.get" \
                  f"?access_token={token}" \
                  f"&v={version}" \
                  f"&domain={domain}" \
                  f"&count={count}" \
                  f"&offset={offset}"
        answer = Request(request)
        return answer


