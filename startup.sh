#!/bin/bash
# Startup Script für PraxisMonitor

echo "=== PraxisMonitor Startup ==="
echo "Überprüfe Cron-Jobs..."

cd /Users/mikagriebsch/Desktop/Programmieren/Mikaskrams/DagmarRossner/PraxisMonitor

# Aktiviere Virtual Environment
source .venv/bin/activate

# Zeige aktive Cron-Jobs
echo "Aktive Cron-Jobs:"
python manage.py crontab show

echo ""
echo "Teste Patient Status Update..."
python manage.py update_patient_status

echo ""
echo "=== Bereit! ==="
echo "Du kannst jetzt den Server starten mit:"
echo "python manage.py runserver"