BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_autotime" (
	"id"	integer NOT NULL,
	"name"	varchar(300) NOT NULL,
	"add_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_chettili" (
	"autotime_ptr_id"	bigint NOT NULL,
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("autotime_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_imkonyat" (
	"autotime_ptr_id"	bigint NOT NULL,
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("autotime_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_qiziqish" (
	"autotime_ptr_id"	bigint NOT NULL,
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("autotime_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_tumanvashahar" (
	"autotime_ptr_id"	bigint NOT NULL,
	"status"	varchar(300) NOT NULL,
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("autotime_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_universitet" (
	"autotime_ptr_id"	bigint NOT NULL,
	"tuman_id"	bigint NOT NULL,
	FOREIGN KEY("tuman_id") REFERENCES "main_tumanvashahar"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("autotime_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_maktabbitiruvchisi" (
	"bitiruvchi_ptr_id"	bigint NOT NULL,
	"sinf"	varchar(300) NOT NULL,
	"univer_sity"	varchar(300),
	"maktab_id"	bigint NOT NULL,
	FOREIGN KEY("maktab_id") REFERENCES "main_maktab"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("bitiruvchi_ptr_id") REFERENCES "main_bitiruvchi"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("bitiruvchi_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_maktab" (
	"autotime_ptr_id"	bigint NOT NULL,
	"status"	varchar(300),
	"tuman_id"	bigint NOT NULL,
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("autotime_ptr_id"),
	FOREIGN KEY("tuman_id") REFERENCES "main_tumanvashahar"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_mahalla" (
	"autotime_ptr_id"	bigint NOT NULL,
	"tuman_id"	bigint NOT NULL,
	PRIMARY KEY("autotime_ptr_id"),
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("tuman_id") REFERENCES "main_tumanvashahar"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_kollej" (
	"autotime_ptr_id"	bigint NOT NULL,
	"tuman_id"	bigint NOT NULL,
	PRIMARY KEY("autotime_ptr_id"),
	FOREIGN KEY("autotime_ptr_id") REFERENCES "main_autotime"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("tuman_id") REFERENCES "main_tumanvashahar"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_bitiruvchi_chettili" (
	"id"	integer NOT NULL,
	"bitiruvchi_id"	bigint NOT NULL,
	"chettili_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("chettili_id") REFERENCES "main_chettili"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("bitiruvchi_id") REFERENCES "main_bitiruvchi"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "main_bitiruvchi_imkonyat" (
	"id"	integer NOT NULL,
	"bitiruvchi_id"	bigint NOT NULL,
	"imkonyat_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("bitiruvchi_id") REFERENCES "main_bitiruvchi"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("imkonyat_id") REFERENCES "main_imkonyat"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "main_bitiruvchi" (
	"id"	integer NOT NULL,
	"f_name"	varchar(300) NOT NULL,
	"img"	varchar(100) NOT NULL,
	"phone"	varchar(9) NOT NULL,
	"email"	varchar(300),
	"guvohnoma"	varchar(300) NOT NULL,
	"idea"	varchar(300) NOT NULL,
	"short_f"	varchar(10000),
	"jins"	varchar(300) NOT NULL,
	"mahalla_id"	bigint NOT NULL,
	"qiziqish_id"	bigint NOT NULL,
	"tuman_id"	bigint NOT NULL,
	"add_time"	datetime NOT NULL,
	"t_sana"	varchar(300),
	FOREIGN KEY("mahalla_id") REFERENCES "main_mahalla"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("qiziqish_id") REFERENCES "main_qiziqish"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("tuman_id") REFERENCES "main_tumanvashahar"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_kollejbitiruvchisi" (
	"bitiruvchi_ptr_id"	bigint NOT NULL,
	"maqsad"	varchar(300) NOT NULL,
	"univer_sity"	varchar(300),
	"kollej_id"	bigint,
	"kolleJ"	varchar(300),
	"stu_way"	varchar(300),
	FOREIGN KEY("kollej_id") REFERENCES "main_kollej"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("bitiruvchi_ptr_id") REFERENCES "main_bitiruvchi"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("bitiruvchi_ptr_id")
);
CREATE TABLE IF NOT EXISTS "main_universitetbitiruvchisi" (
	"bitiruvchi_ptr_id"	bigint NOT NULL,
	"maqsad"	varchar(300) NOT NULL,
	"universitet_id"	bigint,
	"universiteT"	varchar(300),
	"stu_way"	varchar(300),
	FOREIGN KEY("bitiruvchi_ptr_id") REFERENCES "main_bitiruvchi"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("universitet_id") REFERENCES "main_universitet"("autotime_ptr_id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("bitiruvchi_ptr_id")
);
INSERT INTO "django_migrations" VALUES (1,'main','0001_initial','2022-08-16 06:25:46.616038');
INSERT INTO "django_migrations" VALUES (2,'contenttypes','0001_initial','2022-08-16 06:25:57.686788');
INSERT INTO "django_migrations" VALUES (3,'auth','0001_initial','2022-08-16 06:25:57.716789');
INSERT INTO "django_migrations" VALUES (4,'admin','0001_initial','2022-08-16 06:25:57.738794');
INSERT INTO "django_migrations" VALUES (5,'admin','0002_logentry_remove_auto_add','2022-08-16 06:25:57.765792');
INSERT INTO "django_migrations" VALUES (6,'admin','0003_logentry_add_action_flag_choices','2022-08-16 06:25:57.796800');
INSERT INTO "django_migrations" VALUES (7,'contenttypes','0002_remove_content_type_name','2022-08-16 06:25:57.837811');
INSERT INTO "django_migrations" VALUES (8,'auth','0002_alter_permission_name_max_length','2022-08-16 06:25:57.856814');
INSERT INTO "django_migrations" VALUES (9,'auth','0003_alter_user_email_max_length','2022-08-16 06:25:57.874817');
INSERT INTO "django_migrations" VALUES (10,'auth','0004_alter_user_username_opts','2022-08-16 06:25:57.888821');
INSERT INTO "django_migrations" VALUES (11,'auth','0005_alter_user_last_login_null','2022-08-16 06:25:57.919827');
INSERT INTO "django_migrations" VALUES (12,'auth','0006_require_contenttypes_0002','2022-08-16 06:25:57.940833');
INSERT INTO "django_migrations" VALUES (13,'auth','0007_alter_validators_add_error_messages','2022-08-16 06:25:57.954835');
INSERT INTO "django_migrations" VALUES (14,'auth','0008_alter_user_username_max_length','2022-08-16 06:25:57.978841');
INSERT INTO "django_migrations" VALUES (15,'auth','0009_alter_user_last_name_max_length','2022-08-16 06:25:57.995844');
INSERT INTO "django_migrations" VALUES (16,'auth','0010_alter_group_name_max_length','2022-08-16 06:25:58.014849');
INSERT INTO "django_migrations" VALUES (17,'auth','0011_update_proxy_permissions','2022-08-16 06:25:58.031852');
INSERT INTO "django_migrations" VALUES (18,'auth','0012_alter_user_first_name_max_length','2022-08-16 06:25:58.049856');
INSERT INTO "django_migrations" VALUES (19,'sessions','0001_initial','2022-08-16 06:25:58.066860');
INSERT INTO "django_migrations" VALUES (20,'main','0002_bitiruvchi_add_time_alter_bitiruvchi_idea','2022-08-16 06:35:43.227969');
INSERT INTO "django_migrations" VALUES (21,'main','0003_alter_bitiruvchi_email_alter_bitiruvchi_t_sana','2022-08-16 14:19:23.094954');
INSERT INTO "django_migrations" VALUES (22,'main','0004_kollejbitiruvchisi_kollej','2022-08-16 14:30:57.264579');
INSERT INTO "django_migrations" VALUES (23,'main','0005_kollejbitiruvchisi_kollej_and_more','2022-08-16 14:49:10.697244');
INSERT INTO "django_migrations" VALUES (24,'main','0006_kollejbitiruvchisi_stu_way_and_more','2022-08-17 02:21:09.727606');
INSERT INTO "main_autotime" VALUES (1,'Nurafshon','2022-08-16 14:19:38.333016');
INSERT INTO "main_autotime" VALUES (2,'Uchqun','2022-08-16 14:19:49.607050');
INSERT INTO "main_autotime" VALUES (3,'1','2022-08-16 14:19:55.620839');
INSERT INTO "main_autotime" VALUES (4,'2','2022-08-16 14:20:00.098913');
INSERT INTO "main_autotime" VALUES (5,'rus','2022-08-16 14:20:04.965715');
INSERT INTO "main_autotime" VALUES (6,'26','2022-08-16 14:20:13.653725');
INSERT INTO "main_autotime" VALUES (7,'Angeren','2022-08-16 17:05:22.340653');
INSERT INTO "main_autotime" VALUES (8,'Ziyoliylar','2022-08-16 17:05:49.037633');
INSERT INTO "main_autotime" VALUES (9,'9','2022-08-17 01:38:24.538192');
INSERT INTO "main_autotime" VALUES (10,'124','2022-08-17 01:38:29.672509');
INSERT INTO "main_autotime" VALUES (11,'125','2022-08-17 01:38:34.442520');
INSERT INTO "main_chettili" VALUES (5);
INSERT INTO "main_imkonyat" VALUES (4);
INSERT INTO "main_qiziqish" VALUES (3);
INSERT INTO "main_tumanvashahar" VALUES (1,'tuman');
INSERT INTO "main_tumanvashahar" VALUES (7,'shahar');
INSERT INTO "main_maktabbitiruvchisi" VALUES (1,'9-sinf',NULL,6);
INSERT INTO "main_maktab" VALUES (6,'maktab',1);
INSERT INTO "main_maktab" VALUES (9,'maktab',1);
INSERT INTO "main_maktab" VALUES (10,'maktab',7);
INSERT INTO "main_maktab" VALUES (11,'maktab',7);
INSERT INTO "main_mahalla" VALUES (2,1);
INSERT INTO "main_mahalla" VALUES (8,7);
INSERT INTO "main_bitiruvchi_chettili" VALUES (1,1,5);
INSERT INTO "main_bitiruvchi_chettili" VALUES (2,2,5);
INSERT INTO "main_bitiruvchi_chettili" VALUES (3,3,5);
INSERT INTO "main_bitiruvchi_chettili" VALUES (4,4,5);
INSERT INTO "main_bitiruvchi_chettili" VALUES (5,5,5);
INSERT INTO "main_bitiruvchi_chettili" VALUES (6,6,5);
INSERT INTO "main_bitiruvchi_imkonyat" VALUES (1,1,4);
INSERT INTO "main_bitiruvchi_imkonyat" VALUES (2,2,4);
INSERT INTO "main_bitiruvchi_imkonyat" VALUES (3,3,4);
INSERT INTO "main_bitiruvchi_imkonyat" VALUES (4,4,4);
INSERT INTO "main_bitiruvchi_imkonyat" VALUES (5,5,4);
INSERT INTO "main_bitiruvchi_imkonyat" VALUES (6,6,4);
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'main','autotime');
INSERT INTO "django_content_type" VALUES (8,'main','bitiruvchi');
INSERT INTO "django_content_type" VALUES (9,'main','chettili');
INSERT INTO "django_content_type" VALUES (10,'main','imkonyat');
INSERT INTO "django_content_type" VALUES (11,'main','kollej');
INSERT INTO "django_content_type" VALUES (12,'main','maktab');
INSERT INTO "django_content_type" VALUES (13,'main','qiziqish');
INSERT INTO "django_content_type" VALUES (14,'main','tumanvashahar');
INSERT INTO "django_content_type" VALUES (15,'main','universitet');
INSERT INTO "django_content_type" VALUES (16,'main','universitetbitiruvchisi');
INSERT INTO "django_content_type" VALUES (17,'main','maktabbitiruvchisi');
INSERT INTO "django_content_type" VALUES (18,'main','mahalla');
INSERT INTO "django_content_type" VALUES (19,'main','kollejbitiruvchisi');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_autotime','Can add auto time');
INSERT INTO "auth_permission" VALUES (26,7,'change_autotime','Can change auto time');
INSERT INTO "auth_permission" VALUES (27,7,'delete_autotime','Can delete auto time');
INSERT INTO "auth_permission" VALUES (28,7,'view_autotime','Can view auto time');
INSERT INTO "auth_permission" VALUES (29,8,'add_bitiruvchi','Can add bitiruvchi');
INSERT INTO "auth_permission" VALUES (30,8,'change_bitiruvchi','Can change bitiruvchi');
INSERT INTO "auth_permission" VALUES (31,8,'delete_bitiruvchi','Can delete bitiruvchi');
INSERT INTO "auth_permission" VALUES (32,8,'view_bitiruvchi','Can view bitiruvchi');
INSERT INTO "auth_permission" VALUES (33,9,'add_chettili','Can add chet tili');
INSERT INTO "auth_permission" VALUES (34,9,'change_chettili','Can change chet tili');
INSERT INTO "auth_permission" VALUES (35,9,'delete_chettili','Can delete chet tili');
INSERT INTO "auth_permission" VALUES (36,9,'view_chettili','Can view chet tili');
INSERT INTO "auth_permission" VALUES (37,10,'add_imkonyat','Can add imkonyat');
INSERT INTO "auth_permission" VALUES (38,10,'change_imkonyat','Can change imkonyat');
INSERT INTO "auth_permission" VALUES (39,10,'delete_imkonyat','Can delete imkonyat');
INSERT INTO "auth_permission" VALUES (40,10,'view_imkonyat','Can view imkonyat');
INSERT INTO "auth_permission" VALUES (41,11,'add_kollej','Can add kollej');
INSERT INTO "auth_permission" VALUES (42,11,'change_kollej','Can change kollej');
INSERT INTO "auth_permission" VALUES (43,11,'delete_kollej','Can delete kollej');
INSERT INTO "auth_permission" VALUES (44,11,'view_kollej','Can view kollej');
INSERT INTO "auth_permission" VALUES (45,12,'add_maktab','Can add maktab');
INSERT INTO "auth_permission" VALUES (46,12,'change_maktab','Can change maktab');
INSERT INTO "auth_permission" VALUES (47,12,'delete_maktab','Can delete maktab');
INSERT INTO "auth_permission" VALUES (48,12,'view_maktab','Can view maktab');
INSERT INTO "auth_permission" VALUES (49,13,'add_qiziqish','Can add qiziqish');
INSERT INTO "auth_permission" VALUES (50,13,'change_qiziqish','Can change qiziqish');
INSERT INTO "auth_permission" VALUES (51,13,'delete_qiziqish','Can delete qiziqish');
INSERT INTO "auth_permission" VALUES (52,13,'view_qiziqish','Can view qiziqish');
INSERT INTO "auth_permission" VALUES (53,14,'add_tumanvashahar','Can add tuman va shahar');
INSERT INTO "auth_permission" VALUES (54,14,'change_tumanvashahar','Can change tuman va shahar');
INSERT INTO "auth_permission" VALUES (55,14,'delete_tumanvashahar','Can delete tuman va shahar');
INSERT INTO "auth_permission" VALUES (56,14,'view_tumanvashahar','Can view tuman va shahar');
INSERT INTO "auth_permission" VALUES (57,15,'add_universitet','Can add universitet');
INSERT INTO "auth_permission" VALUES (58,15,'change_universitet','Can change universitet');
INSERT INTO "auth_permission" VALUES (59,15,'delete_universitet','Can delete universitet');
INSERT INTO "auth_permission" VALUES (60,15,'view_universitet','Can view universitet');
INSERT INTO "auth_permission" VALUES (61,16,'add_universitetbitiruvchisi','Can add universitet bitiruvchisi');
INSERT INTO "auth_permission" VALUES (62,16,'change_universitetbitiruvchisi','Can change universitet bitiruvchisi');
INSERT INTO "auth_permission" VALUES (63,16,'delete_universitetbitiruvchisi','Can delete universitet bitiruvchisi');
INSERT INTO "auth_permission" VALUES (64,16,'view_universitetbitiruvchisi','Can view universitet bitiruvchisi');
INSERT INTO "auth_permission" VALUES (65,17,'add_maktabbitiruvchisi','Can add maktab bitiruvchisi');
INSERT INTO "auth_permission" VALUES (66,17,'change_maktabbitiruvchisi','Can change maktab bitiruvchisi');
INSERT INTO "auth_permission" VALUES (67,17,'delete_maktabbitiruvchisi','Can delete maktab bitiruvchisi');
INSERT INTO "auth_permission" VALUES (68,17,'view_maktabbitiruvchisi','Can view maktab bitiruvchisi');
INSERT INTO "auth_permission" VALUES (69,18,'add_mahalla','Can add mahalla');
INSERT INTO "auth_permission" VALUES (70,18,'change_mahalla','Can change mahalla');
INSERT INTO "auth_permission" VALUES (71,18,'delete_mahalla','Can delete mahalla');
INSERT INTO "auth_permission" VALUES (72,18,'view_mahalla','Can view mahalla');
INSERT INTO "auth_permission" VALUES (73,19,'add_kollejbitiruvchisi','Can add kollej bitiruvchisi');
INSERT INTO "auth_permission" VALUES (74,19,'change_kollejbitiruvchisi','Can change kollej bitiruvchisi');
INSERT INTO "auth_permission" VALUES (75,19,'delete_kollejbitiruvchisi','Can delete kollej bitiruvchisi');
INSERT INTO "auth_permission" VALUES (76,19,'view_kollejbitiruvchisi','Can view kollej bitiruvchisi');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$320000$upocmkK61g9qHvVoyXqfyq$Wf7f+vbb4Zv9sNnORXYHSoucnXouJ9OgjM6+0DIiTGA=','2022-08-17 01:20:00.086610',1,'Zohidillo','','',1,1,'2022-08-16 06:26:27.657716','');
INSERT INTO "django_session" VALUES ('tv47sb1sh23shbz508p8c2mxtbruw2fa','.eJxVjDsOwjAQBe_iGln-xl5Kes5g7XotHEC2FCcV4u4QKQW0b2beSyTc1pq2UZY0szgLLU6_G2F-lLYDvmO7dZl7W5eZ5K7Igw557Vyel8P9O6g46remyRJkAMvBEztn3AQhA0ZjOUZtgs-KCpCxnnUEH3RAZbJ12qmI5MT7A8W_Nrw:1oO7iy:zL3ZkojmVF50ap2USaj0Qgyykn_b5JAUjHleg6HH3Tc','2022-08-31 01:20:00.103537');
INSERT INTO "main_bitiruvchi" VALUES (1,'Bekjon Muradov','default/default.png','904561274',NULL,'Yoq','Bor',NULL,'o''g''il bola',2,3,1,'2022-08-16 14:20:40.561001',NULL);
INSERT INTO "main_bitiruvchi" VALUES (2,'Bekjon Muradov','default/default.png','909905786',NULL,'Bor','Bor',NULL,'o''g''il bola',2,3,1,'2022-08-16 14:51:55.752341',NULL);
INSERT INTO "main_bitiruvchi" VALUES (3,'Akmal kadirov','default/default.png','904561274',NULL,'Yoq','Bor',NULL,'o''g''il bola',2,3,1,'2022-08-16 15:29:11.306692',NULL);
INSERT INTO "main_bitiruvchi" VALUES (4,'Bekjon Muradov','default/default.png','904561274',NULL,'Yoq','Bor',NULL,'o''g''il bola',2,3,1,'2022-08-16 15:29:49.625055',NULL);
INSERT INTO "main_bitiruvchi" VALUES (5,'Akmal kadirov','default/default.png','904561274',NULL,'Yoq','Bor',NULL,'o''g''il bola',8,3,7,'2022-08-16 17:06:22.006589',NULL);
INSERT INTO "main_bitiruvchi" VALUES (6,'Jamshid','default/default.png','904561274',NULL,'Yoq','Bor',NULL,'o''g''il bola',8,3,7,'2022-08-17 01:57:15.404009',NULL);
INSERT INTO "main_kollejbitiruvchisi" VALUES (2,'Ishlamoqchi',NULL,NULL,'kollej',NULL);
INSERT INTO "main_kollejbitiruvchisi" VALUES (3,'Ishlamoqchi',NULL,NULL,'kollej1',NULL);
INSERT INTO "main_kollejbitiruvchisi" VALUES (5,'Ishlamoqchi',NULL,NULL,'Kollej3',NULL);
INSERT INTO "main_universitetbitiruvchisi" VALUES (4,'Ishlamoqchi',NULL,'otm',NULL);
INSERT INTO "main_universitetbitiruvchisi" VALUES (6,'Ishlamoqchi',NULL,'tatu',NULL);
CREATE INDEX IF NOT EXISTS "main_universitet_tuman_id_eeb3dc39" ON "main_universitet" (
	"tuman_id"
);
CREATE INDEX IF NOT EXISTS "main_maktabbitiruvchisi_maktab_id_480af2d2" ON "main_maktabbitiruvchisi" (
	"maktab_id"
);
CREATE INDEX IF NOT EXISTS "main_maktab_tuman_id_01e94351" ON "main_maktab" (
	"tuman_id"
);
CREATE INDEX IF NOT EXISTS "main_mahalla_tuman_id_d1598a91" ON "main_mahalla" (
	"tuman_id"
);
CREATE INDEX IF NOT EXISTS "main_kollej_tuman_id_525b3970" ON "main_kollej" (
	"tuman_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "main_bitiruvchi_chettili_bitiruvchi_id_chettili_id_29df1071_uniq" ON "main_bitiruvchi_chettili" (
	"bitiruvchi_id",
	"chettili_id"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_chettili_bitiruvchi_id_3a4e6f1b" ON "main_bitiruvchi_chettili" (
	"bitiruvchi_id"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_chettili_chettili_id_79d89fbb" ON "main_bitiruvchi_chettili" (
	"chettili_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "main_bitiruvchi_imkonyat_bitiruvchi_id_imkonyat_id_b89db6c4_uniq" ON "main_bitiruvchi_imkonyat" (
	"bitiruvchi_id",
	"imkonyat_id"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_imkonyat_bitiruvchi_id_d4724e2a" ON "main_bitiruvchi_imkonyat" (
	"bitiruvchi_id"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_imkonyat_imkonyat_id_4dd66d00" ON "main_bitiruvchi_imkonyat" (
	"imkonyat_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_mahalla_id_e85fef36" ON "main_bitiruvchi" (
	"mahalla_id"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_qiziqish_id_edf81d13" ON "main_bitiruvchi" (
	"qiziqish_id"
);
CREATE INDEX IF NOT EXISTS "main_bitiruvchi_tuman_id_b35ba060" ON "main_bitiruvchi" (
	"tuman_id"
);
CREATE INDEX IF NOT EXISTS "main_kollejbitiruvchisi_kollej_id_2991b66d" ON "main_kollejbitiruvchisi" (
	"kollej_id"
);
CREATE INDEX IF NOT EXISTS "main_universitetbitiruvchisi_universitet_id_a194887c" ON "main_universitetbitiruvchisi" (
	"universitet_id"
);
COMMIT;
