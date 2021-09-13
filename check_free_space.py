import shutil
import json
import requests
from config import SLACK_WEBHOOK_URL

def send_report_to_slack():
    total, used, free = shutil.disk_usage("/")
    total_space_in_gb = total// (2**30)
    used_space_in_gb = used// (2**30)
    free_space_in_gb = free// (2**30)
    if free_space_in_gb < 1000:
        title_of_notification = f'Внимание, заканчивается место на сервере!!!'
        message_text = f'Total: {total_space_in_gb} GiB\nUsed: {used_space_in_gb} GiB\nFree: {free_space_in_gb} GiB'

        payload = {
            'attachments': [
                {
                    'fallback': title_of_notification,
                    'pretext': message_text,
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
        }
        requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload, indent=4), headers=headers)


if __name__ == '__main__':
    send_report_to_slack()