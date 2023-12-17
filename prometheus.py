# Configuration globale pour Prometheus
global:
  scrape_interval: 15s  # Intervalle de base pour collecter les métriques (ici, toutes les 15 secondes)

# Configuration des jobs de scraping
scrape_configs:
  # Job de scraping pour Prometheus lui-même
  - job_name: 'prometheus'  # Nom du job
    scrape_interval: 15s   # Intervalle de scraping pour ce job (toutes les 15 secondes)
    metrics_path: /prometheus/metrics  # Chemin pour accéder aux métriques exposées par Prometheus
    static_configs:  # Configurations statiques pour les cibles à scraper
      - targets: ['localhost:9090']  # Cibles à scraper (Prometheus sur localhost au port 9090)

  # Job de scraping pour l'application 'app'
  - job_name: 'app'  # Nom du job
    scrape_interval: 5s  # Intervalle de scraping pour ce job (toutes les 5 secondes)
    static_configs:  # Configurations statiques pour les cibles à scraper
      - targets: ['app:8000']  # Cibles à scraper (application 'app' au port 8000)