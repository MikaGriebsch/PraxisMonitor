#!/bin/bash
# PraxisMonitor Start/Stop Script

cd /Users/mikagriebsch/Desktop/Programmieren/Mikaskrams/DagmarRossner/PraxisMonitor

case "$1" in
    start)
        echo "🚀 Starte PraxisMonitor..."
        source .venv/bin/activate
        python manage.py crontab add
        echo "✅ Automatische Patientenstatus-Aktualisierung aktiviert (alle 2 Min)"
        echo "Du kannst jetzt den Server starten:"
        echo "python manage.py runserver"
        ;;
    stop)
        echo "🛑 Stoppe PraxisMonitor..."
        source .venv/bin/activate
        python manage.py crontab remove
        echo "✅ Automatische Aktualisierung gestoppt"
        echo "Dein Mac wird nicht mehr belastet."
        ;;
    status)
        echo "📊 PraxisMonitor Status:"
        source .venv/bin/activate
        python manage.py crontab show
        ;;
    *)
        echo "Verwendung: $0 {start|stop|status}"
        echo "  start  - Startet die automatische Patientenstatus-Aktualisierung"
        echo "  stop   - Stoppt die automatische Aktualisierung"
        echo "  status - Zeigt den aktuellen Status"
        ;;
esac