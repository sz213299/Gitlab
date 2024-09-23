SET FOREIGN_KEY_CHECKS=0;



INSERT INTO `front_author`  VALUES (1,'曹雪芹', '1715', 'caoxueqin@example.com');
INSERT INTO `front_author`  VALUES (2,'罗贯中', '1330', 'luoguanzhong@example.com');
INSERT INTO `front_author`  VALUES (3,'施耐庵', '1296', 'shinaian@example.com');
INSERT INTO `front_author`  VALUES (4,'吴承恩', '1500', 'wuchengen@example.com');




INSERT INTO `front_Book`  VALUES ('1','红楼梦', '120', '99.99', '9.5', '1', '1');
INSERT INTO `front_Book`  VALUES ('2','三国演义', '120', '89.99', '9.2', '2', '1');
INSERT INTO `front_Book`  VALUES ('3','水浒传', '100', '79.99', '9.0', '3', '1');
INSERT INTO `front_Book`  VALUES ('4','西游记', '100', '69.99', '8.8', '4', '1');




INSERT INTO `front_BookOrder`  VALUES ('1', '99.99','1');
INSERT INTO `front_BookOrder`  VALUES ('2', '89.99','1');
INSERT INTO `front_BookOrder`  VALUES ('3', '79.99','2');
INSERT INTO `front_BookOrder`  VALUES ('4', '69.99','2');



INSERT INTO `front_publisher`  VALUES ('1','中国');
INSERT INTO `front_publisher`  VALUES ('2','清华');