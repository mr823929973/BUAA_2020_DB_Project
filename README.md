# BUAA_2020_DB_Project

### How to deploy
+ install require packages
```
    conda install --file requiements.txt
     or // pip intsall -r requirements.txt
```
+ create a database in mysql
```
CREATE DATABASE IF NOT EXISTS DBjwxt DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```
+ configure
```
python manage.py makemigrations
python manage.py migrate
```

+ run
```
python manage.py runserver 0.0.0.0:80
```

```mysql
CREATE TRIGGER TCdeleted AFTER DELETE ON dbmodels_sc FOR EACH ROW 
	UPDATE dbmodels_tc SET s = (SELECT COUNT(*) FROM dbmodels_sc 
                                WHERE tc_id = NEW.tc_id) WHERE id = NEW.tc_id;

```

