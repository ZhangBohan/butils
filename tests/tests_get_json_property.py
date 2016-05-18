import unittest

from butils import get_json_property


class JsonPropertyTest(unittest.TestCase):
    def test_data(self):
        data = {
            "foo": "bar",
            "a": {"b": "c", "l": [{"d": "e"}, {"f": "g"}]}
        }

        self.assertEqual(get_json_property(data=data, property_str='foo'), 'bar')
        self.assertEqual(get_json_property(data=data, property_str='a.b'), 'c')
        self.assertEqual(get_json_property(data=data, property_str='a.l[0].d'), 'e')

    def test_json_str(self):
        json_str = '{"data": {"users": [{"avatar_url": "http://7xjnx1.com2.z0.glb.qiniucdn.com/11d53398-356a-46b8-a48a-94b9a106b763", "bio": "Life is a cycle", "easemob_username": "32636526595", "id": 32636526595, "is_agent": false, "is_blacklisted": false, "live_broadcast_id": null, "location": null, "n_broadcasts": 153, "n_followers": 61, "n_following": 129, "n_like_received": 2503129, "n_seconds_broadcasting": 12486, "n_seconds_watching": 13057, "personal_url": "https://zaizhibo.tv/bohan", "sharing_kvs": {"facebook_content": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0", "facebook_image": "http://7xjnx1.com2.z0.glb.qiniucdn.com/11d53398-356a-46b8-a48a-94b9a106b763", "facebook_title": "\\u4f2f\\u51fd\'s live station", "facebook_url": "https://zaizhibo.tv/bohan", "qq_content": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0", "qq_image": "http://7xjnx1.com2.z0.glb.qiniucdn.com/11d53398-356a-46b8-a48a-94b9a106b763", "qq_title": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0", "qq_url": "https://zaizhibo.tv/bohan", "twitter_content": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0", "twitter_image": "http://7xjnx1.com2.z0.glb.qiniucdn.com/11d53398-356a-46b8-a48a-94b9a106b763", "twitter_title": "\\u4f2f\\u51fd\'s live station", "twitter_url": "https://zaizhibo.tv/bohan", "weibo_content": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0 @\\u5728\\u76f4\\u64adapp https://zaizhibo.tv/bohan", "weibo_image": "http://7xjnx1.com2.z0.glb.qiniucdn.com/11d53398-356a-46b8-a48a-94b9a106b763", "weixin_content": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0 @\\u5728\\u76f4\\u64adapp https://zaizhibo.tv/bohan", "weixin_image": "http://7xjnx1.com2.z0.glb.qiniucdn.com/11d53398-356a-46b8-a48a-94b9a106b763", "weixin_title": "\\u4f2f\\u51fd\\u7684\\u76f4\\u64ad\\u53f0", "weixin_url": "https://zaizhibo.tv/bohan"}, "slug": "bohan", "user_level": 3, "username": "\\u4f2f\\u51fd", "vip_level": "ip"}, null, null, null, null, null, null, null]}, "meta": {"hostname": "app40", "success": true}}'
        self.assertEqual(get_json_property(data=json_str, property_str='data.users[0].bio'), 'Life is a cycle')
