# Meriç Kaya – Portfolyo / Portfolio

[Türkçe](#türkçe) · [English](#english)

---

## Türkçe

Kendimi, ilgi alanlarımı ve projelerimi tanıttığım, Django ile geliştirilmiş kişisel portfolyo sitesi. Site Türkçe ve İngilizce olarak kullanılabilir. İçeriğin tamamı Django admin panelinden yönetilir.

### Özellikler

- **İki dil desteği (TR / EN):** Arayüz metinleri Django i18n ile, veritabanı içerikleri `django-modeltranslation` ile çevrilir. Dil, menüdeki seçiciden değiştirilir.
- **Admin panelinden içerik yönetimi:** Profil, hobiler, projeler, kodlama dilleri ve iletişim bağlantıları kod değiştirmeden eklenip düzenlenebilir.
- **Ortam değişkenleri:** `SECRET_KEY` ve `DEBUG` değerleri `.env` dosyasından okunur.

### Sayfa Bölümleri

- **Anasayfa** – Karşılama ekranı ve profil fotoğrafı
- **Hakkımda** – Kişisel bilgiler, bildiğim kodlama dilleri ve hakkımda yazısı
- **Hobilerim & İlgilerim** – Admin panelinden eklenen hobiler
- **Projelerim** – Admin panelinden eklenen projeler
- **Bağlantılar** – LinkedIn, GitHub gibi iletişim bağlantıları

### Projeler

| Proje | Açıklama | Bağlantılar |
|-------|----------|-------------|
| **Django Multi-Vendor E-Ticaret** | Django ile geliştirdiğim çok satıcılı e-ticaret sitesi. Sepet, PayPal Sandbox ile ödeme, satıcı paneli, ürün yorumları ve istek listesi içerir. AWS Elastic Beanstalk ve MySQL (AWS RDS) üzerinde çalışır. | [Canlı site](http://djangoecommerce-env.eba-mjr8eytm.eu-north-1.elasticbeanstalk.com/) · [Kaynak kod](https://github.com/merickayaa/Django-Multivendor-Ecommerce) |
| **BAUN Media** | Django ile geliştirdiğim sosyal medya sitesi | [Canlı site](http://baun-media.eu-north-1.elasticbeanstalk.com/) · [Kaynak kod](https://github.com/merickayaa/Django-Social-Media) |

### Kullanılan Teknolojiler

- Python, Django 5.2
- django-modeltranslation
- SQLite
- HTML5, CSS3, JavaScript
- [Bootstrap 5](https://getbootstrap.com/)

### Kurulum

1. Repoyu klonlayın:
   ```bash
   git clone https://github.com/merickayaa/Portfolio.git
   cd Portfolio
   ```
2. Sanal ortam oluşturup etkinleştirin:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
3. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. Proje klasöründe bir `.env` dosyası oluşturun:
   ```env
   SECRET_KEY=gizli-bir-anahtar
   DEBUG=True
   ```
5. Veritabanını oluşturun ve bir admin kullanıcısı ekleyin:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Sunucuyu başlatın:
   ```bash
   python manage.py runserver
   ```
7. `http://127.0.0.1:8000/admin/` adresinden giriş yapıp bir **Profile** kaydı oluşturun. Anasayfa ilk profil kaydını (`id=1`) gösterir, kayıt yoksa sayfa hata verir. Ardından hobi, proje, kodlama dili ve iletişim bağlantılarını ekleyin.

### Klasör Yapısı

```
Portfolio/
├── core/            # Ana uygulama: modeller, view'lar, admin ve çeviri ayarları
├── portfolio/       # Proje ayarları ve URL yapılandırması
├── templates/       # HTML şablonları
├── static/img/      # Sabit görseller
├── locale/          # Arayüz çeviri dosyaları (tr, en)
├── manage.py
└── requirements.txt
```

### İletişim

- **E-posta:** merickay0@yandex.com
- **LinkedIn:** [Meriç Kaya](https://www.linkedin.com/in/meri%C3%A7-kaya-883b08269/)
- **GitHub:** [merickayaa](https://github.com/merickayaa)

---

## English

My personal portfolio website, built with Django, where I introduce myself, my interests and my projects. The site is available in Turkish and English, and all of its content is managed from the Django admin panel.

### Features

- **Bilingual (TR / EN):** Interface text is translated with Django i18n, and database content with `django-modeltranslation`. The language can be switched from the selector in the menu.
- **Content managed from the admin panel:** The profile, hobbies, projects, programming languages and contact links can be added and edited without touching the code.
- **Environment variables:** `SECRET_KEY` and `DEBUG` are read from a `.env` file.

### Page Sections

- **Home** – Welcome screen and profile photo
- **About Me** – Personal information, the programming languages I know and an about me text
- **Hobbies & Interests** – Hobbies added from the admin panel
- **Projects** – Projects added from the admin panel
- **Links** – Contact links such as LinkedIn and GitHub

### Projects

| Project | Description | Links |
|---------|-------------|-------|
| **Django Multi-Vendor E-Commerce** | A multi-vendor e-commerce website built with Django. Includes a shopping cart, checkout with PayPal Sandbox, a vendor dashboard, product reviews and a wishlist. Runs on AWS Elastic Beanstalk with MySQL (AWS RDS). | [Live site](http://djangoecommerce-env.eba-mjr8eytm.eu-north-1.elasticbeanstalk.com/) · [Source code](https://github.com/merickayaa/Django-Multivendor-Ecommerce) |
| **BAUN Media** | A social media website built with Django | [Live site](http://baun-media.eu-north-1.elasticbeanstalk.com/) · [Source code](https://github.com/merickayaa/Django-Social-Media) |

### Technologies Used

- Python, Django 5.2
- django-modeltranslation
- SQLite
- HTML5, CSS3, JavaScript
- [Bootstrap 5](https://getbootstrap.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/merickayaa/Portfolio.git
   cd Portfolio
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project folder:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```
5. Create the database and an admin user:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
7. Log in at `http://127.0.0.1:8000/admin/` and create a **Profile** entry. The home page shows the first profile (`id=1`) and returns an error if it does not exist. Then add your hobbies, projects, programming languages and contact links.

### Folder Structure

```
Portfolio/
├── core/            # Main app: models, views, admin and translation settings
├── portfolio/       # Project settings and URL configuration
├── templates/       # HTML templates
├── static/img/      # Static images
├── locale/          # Interface translation files (tr, en)
├── manage.py
└── requirements.txt
```

### Contact

- **Email:** merickay0@yandex.com
- **LinkedIn:** [Meriç Kaya](https://www.linkedin.com/in/meri%C3%A7-kaya-883b08269/)
- **GitHub:** [merickayaa](https://github.com/merickayaa)
