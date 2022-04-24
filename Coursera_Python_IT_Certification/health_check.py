import psutil
import socket
import emails

# set system thresholds:
max_cpu_usage_perc = 80
max_disk_avail_perc = 20
max_mem_avail_mb = 500
chk_local_host_ip = "127.0.0.1"


def check_CPU():
    cpu_usage_perc = psutil.cpu_percent(interval=3)
    return cpu_usage_perc > max_cpu_usage_perc


def check_Disk():
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    return dsk_usage_perc > max_disk_usage_perc


def check_memory():
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_mem_avail_mb
    mem_avail = psutil.virtual_memory().available
    return mem_avail < max_mem_avail


def check_network():
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != chk_local_host_ip


def sendAlert(alert):
    content = {
        "sender": "automation@example.com",
        "receiver": "student-03-6062af701fc1@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    try:
        message = emails.generate_email(**content)
        emails.send_email(message)
    except:
        print("unable to send alert email notification!")
    finally:
        print(alert)
        exit(1)


def main():
    print("checking system resources")
    alert = None
    if check_CPU():
        alert = f"Error - CPU usage is over {max_cpu_usage_perc}%"
    elif check_Disk():
        alert = f"Error - Available disk space is less than {max_disk_avail_perc}%"
    elif check_memory():
        alert = f"Error - Available memory is less than {max_mem_avail_mb}MB"
    elif check_network():
        alert = f"Error - localhost cannot be resolved to {chk_local_host_ip}"

    #Alert
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()