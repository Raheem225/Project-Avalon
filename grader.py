import requests

GRAFANA_URL = "https://raheemsalam.grafana.net/public-dashboards/b4d64142ca4a4c0b8ca2f3e5dad6e989"
API_KEY = "xyyxyxyxyxyyxyyyx"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_dashboard(uid):
    url = f"{GRAFANA_URL}/api/dashboards/uid/{uid}"
    return requests.get(url, headers=headers).json()

def check_panels(dashboard):
    panels = dashboard['dashboard']['panels']
    
    checks = {
        "has_stat_panel": False,
        "has_pie_chart": False,
        "has_time_override": False
    }

    for panel in panels:
        if panel['type'] == 'stat':
            checks["has_stat_panel"] = True
        if panel['type'] == 'piechart':
            checks["has_pie_chart"] = True
        if 'timeFrom' in panel:
            checks["has_time_override"] = True

    return checks

if __name__ == "__main__":
    dashboard = get_dashboard("dashboard_uid")
    results = check_panels(dashboard)
    print(results)