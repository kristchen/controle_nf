PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "core_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "cnpj" varchar(18) NOT NULL UNIQUE, "password" varchar(255) NOT NULL, "company_name" varchar(255) NOT NULL, "phone_number" varchar(20) NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL, "is_active" bool NOT NULL, "is_staff" bool NOT NULL, "is_superuser" bool NOT NULL, "last_login" datetime NULL, "last_name" varchar(150) NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "email" varchar(255) NOT NULL UNIQUE);
INSERT INTO core_user VALUES(1,'Master User','89898305000176','pbkdf2_sha256$260000$fY1WcCCHVryLaSwWuMu2jO$Gc7VIyzKvs1yBGUL+JlzkF68jjtXUPWE4aMzsP3nSnk=','Master INC','111111111','2021-10-19 18:24:40.483655','',1,0,0,NULL,'','master','master@master.com');
COMMIT;
