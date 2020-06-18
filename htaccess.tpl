<IfModule mod_rewrite.c>
RewriteEngine on
RewriteCond %{HTTP_HOST} ^{{origin_domain}}$ [OR]
RewriteCond %{HTTP_HOST} ^www.{{origin_domain}}$
RewriteRule ^(.*)$ {{new_domain_with_protocol}}/$1 [R=301,L]

</IfModule>