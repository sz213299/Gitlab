import requests

headers = {
    "sec-ch-ua-platform": "\"Windows\"",
    "Referer": "https://www.douyin.com/user/MS4wLjABAAAArEVLEa-OxHisbIVsn3i3UwQZpIYkTGg1Dmp5M77NG_0?from_tab_name=main&vid=7425203786492218687",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0"
}
url = "https://www.douyin.com/aweme/v1/web/aweme/post/"
params = {
    "device_platform": "webapp",
    "aid": "6383",
    "channel": "channel_pc_web",
    "sec_user_id": "MS4wLjABAAAArEVLEa-OxHisbIVsn3i3UwQZpIYkTGg1Dmp5M77NG_0",
    "max_cursor": "0",
    "locate_item_id": "7425203786492218687",
    "locate_query": "false",
    "show_live_replay_strategy": "1",
    "need_time_list": "1",
    "time_list_query": "0",
    "whale_cut_token": "",
    "cut_version": "1",
    "count": "18",
    "publish_video_strategy_type": "2",
    "from_user_page": "1",
    "update_version_code": "170400",
    "pc_client_type": "1",
    "pc_libra_divert": "Windows",
    "version_code": "290100",
    "version_name": "29.1.0",
    "cookie_enabled": "true",
    "screen_width": "1494",
    "screen_height": "934",
    "browser_language": "zh-CN",
    "browser_platform": "Win32",
    "browser_name": "Chrome",
    "browser_version": "129.0.0.0",
    "browser_online": "true",
    "engine_name": "Blink",
    "engine_version": "129.0.0.0",
    "os_name": "Windows",
    "os_version": "10",
    "cpu_core_num": "12",
    "device_memory": "8",
    "platform": "PC",
    "downlink": "10",
    "effective_type": "4g",
    "round_trip_time": "150",
    "webid": "7425889640172832266",
    "a_bogus": "Q645gF7ympWfcVFGucb4tG-Uc1I/rPuyA3iQRHHP9OY7bZUO8bPhoNe8jxoi48EDtRphh9IH0delbDxcPzXhZ9npompDuwtbaU2V9gvLMqNXalk0LHRse0vFzwMFlY4ElA9GN1mR1s0xgVQ-9HV0WpdGH5FqmbRZSHZ3dMb9nDSWpTgT9x/Heagh",
    "verifyFp": "verify_m2a2vx2e_0wF9vtkx_kIEp_407R_9n7P_E5WXB2cesQMq",
    "fp": "verify_m2a2vx2e_0wF9vtkx_kIEp_407R_9n7P_E5WXB2cesQMq"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
