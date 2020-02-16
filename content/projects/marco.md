Title: Marco Eco Discounter
Date: 2019-09-01
Tags: django, saleor, postgresql, celery
Slug: marco
Cover: projects/img/marco-home.png
Link: https://marco.kz/
Contribution: Sole backend developer
Summary: E-commerce grocery store

This project was developed as part of a physical grocery store chain's strategy to go online. Online store successfully served hundreds of customers since it's commercial launch and offers 30K+ different products.

![Home page]({attach}img/marco-home.png)

Online store was built on top of Saleor e-commerce platform which is based on Django.
Lots of customizations has been made to initial platform in order to meet customer's specific business needs:

- Ability to rate and review products. Dashboard interface for moderating product reviews
- Designed custom order workflow. Customer and manager notifications on each step
- Scheduled ETL cronjob for synchronising products stock and prices with customer's ERP system (powered by Celery). Displaying results in dashboard
- Account registration verification using OTP. Integration with SMS gateway
- Custom middleware for showing age-restricted products only to adult customers
- Added support for business customers
- Integration with MailChimp for subscription to email lists
- Built-in product and variant models has been extended to support customer's SKU and Barcode data in ERP
- Custom dashboard interfaces to support translation of all models to 3 languages: English, Kazakh, Russian


*Checkout:*
![Checkout]({attach}img/marco-checkout.png)

*Dashboard:*
![Dashboard]({attach}img/marco-dashboard.png)
