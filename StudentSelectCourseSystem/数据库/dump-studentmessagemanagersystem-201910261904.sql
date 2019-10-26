-- MySQL dump 10.13  Distrib 8.0.15, for Linux (x86_64)
--
-- Host: localhost    Database: studentmessagemanagersystem
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_control`
--

DROP TABLE IF EXISTS `tb_control`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_control` (
  `IfTakeCourse` char(1) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `IfInputGrade` char(1) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_control`
--

LOCK TABLES `tb_control` WRITE;
/*!40000 ALTER TABLE `tb_control` DISABLE KEYS */;
INSERT INTO `tb_control` VALUES ('1','1',0);
/*!40000 ALTER TABLE `tb_control` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_course`
--

DROP TABLE IF EXISTS `tb_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_course` (
  `CourseNum` varchar(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `CourseName` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `CourseCredit` float(20,0) NOT NULL,
  `CourseClass` smallint(20) NOT NULL,
  `CourseTeacherNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`CourseNum`),
  KEY `hhh` (`CourseTeacherNum`),
  CONSTRAINT `hhh` FOREIGN KEY (`CourseTeacherNum`) REFERENCES `tb_teacher` (`teachernum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_course`
--

LOCK TABLES `tb_course` WRITE;
/*!40000 ALTER TABLE `tb_course` DISABLE KEYS */;
INSERT INTO `tb_course` VALUES ('002','英语',3,16,'001'),('003','web',3,5,'001'),('004','java',3,5,'001'),('031','高等数学',0,48,'111'),('44','语文',3,4,'001'),('55','看来',3,4,'111');
/*!40000 ALTER TABLE `tb_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dept`
--

DROP TABLE IF EXISTS `tb_dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_dept` (
  `DeptNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `DeptName` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `DeptChairman` varchar(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `DeptTel` varchar(15) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `DeptDesc` text CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`DeptNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dept`
--

LOCK TABLES `tb_dept` WRITE;
/*!40000 ALTER TABLE `tb_dept` DISABLE KEYS */;
INSERT INTO `tb_dept` VALUES ('131','计算机学院','呵呵','123456666','.。。');
/*!40000 ALTER TABLE `tb_dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_major`
--

DROP TABLE IF EXISTS `tb_major`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_major` (
  `MajorNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `DeptNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `MajorName` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `MajorAssistant` varchar(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `MajorTel` varchar(15) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`MajorNum`),
  KEY `DeptNum` (`DeptNum`),
  CONSTRAINT `tb_major_ibfk_1` FOREIGN KEY (`DeptNum`) REFERENCES `tb_dept` (`DeptNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_major`
--

LOCK TABLES `tb_major` WRITE;
/*!40000 ALTER TABLE `tb_major` DISABLE KEYS */;
INSERT INTO `tb_major` VALUES ('015','131','软件工程','张','00121');
/*!40000 ALTER TABLE `tb_major` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_manager`
--

DROP TABLE IF EXISTS `tb_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_manager` (
  `ManagerNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `ManagerName` varchar(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `ManagerSex` char(2) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `ManagerBirthdate` datetime NOT NULL,
  `ManagerRights` int(11) NOT NULL,
  `ManagerPassword` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`ManagerNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_manager`
--

LOCK TABLES `tb_manager` WRITE;
/*!40000 ALTER TABLE `tb_manager` DISABLE KEYS */;
INSERT INTO `tb_manager` VALUES ('001','为','男','2018-12-27 15:43:54',11,'12345');
/*!40000 ALTER TABLE `tb_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_stucourse`
--

DROP TABLE IF EXISTS `tb_stucourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_stucourse` (
  `StudentNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `CourseNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `TeacherNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `Grade` smallint(6) unsigned DEFAULT NULL,
  KEY `StudentNum` (`StudentNum`),
  KEY `CourseNum` (`CourseNum`),
  KEY `TeacherNum` (`TeacherNum`),
  CONSTRAINT `tb_stucourse_ibfk_1` FOREIGN KEY (`StudentNum`) REFERENCES `tb_student` (`studentnum`),
  CONSTRAINT `tb_stucourse_ibfk_2` FOREIGN KEY (`CourseNum`) REFERENCES `tb_course` (`CourseNum`),
  CONSTRAINT `tb_stucourse_ibfk_3` FOREIGN KEY (`TeacherNum`) REFERENCES `tb_teacher` (`teachernum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_stucourse`
--

LOCK TABLES `tb_stucourse` WRITE;
/*!40000 ALTER TABLE `tb_stucourse` DISABLE KEYS */;
INSERT INTO `tb_stucourse` VALUES ('11412','031','111',NULL),('002','002','001',NULL),('003','002','001',100),('111','002','001',1),('001','55','111',NULL),('001','004','001',NULL),('001','002','001',NULL),('11412','55','111',NULL),('11412','004','001',NULL),('11412','003','001',50);
/*!40000 ALTER TABLE `tb_stucourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_student`
--

DROP TABLE IF EXISTS `tb_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_student` (
  `StudentNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `MajorNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `StudentName` varchar(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci DEFAULT NULL,
  `StudentSex` char(2) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `StudentBirthday` datetime NOT NULL,
  `StudentPassword` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`StudentNum`),
  KEY `MajorNum` (`MajorNum`),
  CONSTRAINT `tb_student_ibfk_1` FOREIGN KEY (`MajorNum`) REFERENCES `tb_major` (`MajorNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_student`
--

LOCK TABLES `tb_student` WRITE;
/*!40000 ALTER TABLE `tb_student` DISABLE KEYS */;
INSERT INTO `tb_student` VALUES ('001','015','还好','男','2018-12-06 15:52:57','1234'),('002','015','还好','男','2018-12-06 00:00:00','12345'),('003','015','还好','男','2018-12-06 00:00:00','12345'),('111','015','李腾飞','男','2018-12-06 22:19:54','12345'),('11314','015','李白','女','2018-12-06 15:52:57','12315'),('11412','015','王刚','男','2018-12-25 15:41:01','12345'),('12345','015','宝宝','男','2018-12-06 15:52:57','12567'),('14567','015','joke','男','1995-04-12 00:00:00','12345'),('14568','015','joke','男','1995-04-12 00:00:00','12345'),('337','015','55','女','2016-05-16 00:00:00','777');
/*!40000 ALTER TABLE `tb_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_teacher`
--

DROP TABLE IF EXISTS `tb_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_teacher` (
  `TeacherNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `DeptNum` char(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `TeacherName` varchar(10) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `TeacherSex` char(2) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  `TeacherBirthday` datetime NOT NULL,
  `TeacherTitle` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci DEFAULT NULL,
  `TeacherPassword` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci NOT NULL,
  PRIMARY KEY (`TeacherNum`),
  KEY `DeptNum` (`DeptNum`),
  CONSTRAINT `tb_teacher_ibfk_1` FOREIGN KEY (`DeptNum`) REFERENCES `tb_dept` (`DeptNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_croatian_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_teacher`
--

LOCK TABLES `tb_teacher` WRITE;
/*!40000 ALTER TABLE `tb_teacher` DISABLE KEYS */;
INSERT INTO `tb_teacher` VALUES ('001','131','快快','女','2016-08-09 00:00:00','教师','12345'),('111','131','李','女','2018-12-12 15:42:12','教授','12345'),('55','131','lk','男','2018-05-15 00:00:00','老师','567');
/*!40000 ALTER TABLE `tb_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vi_grade`
--

DROP TABLE IF EXISTS `vi_grade`;
/*!50001 DROP VIEW IF EXISTS `vi_grade`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `vi_grade` AS SELECT 
 1 AS `StudentNum`,
 1 AS `StudentName`,
 1 AS `CourseName`,
 1 AS `CourseCredit`,
 1 AS `TeacherName`,
 1 AS `Grade`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vi_major`
--

DROP TABLE IF EXISTS `vi_major`;
/*!50001 DROP VIEW IF EXISTS `vi_major`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `vi_major` AS SELECT 
 1 AS `MajorName`,
 1 AS `StudentNum`,
 1 AS `StudentName`,
 1 AS `StudentSex`,
 1 AS `StudentBirthday`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'studentmessagemanagersystem'
--

--
-- Final view structure for view `vi_grade`
--

/*!50001 DROP VIEW IF EXISTS `vi_grade`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_grade` AS select `tb_stucourse`.`StudentNum` AS `StudentNum`,`tb_student`.`StudentName` AS `StudentName`,`tb_course`.`CourseName` AS `CourseName`,`tb_course`.`CourseCredit` AS `CourseCredit`,`tb_teacher`.`TeacherName` AS `TeacherName`,`tb_stucourse`.`Grade` AS `Grade` from (((`tb_stucourse` join `tb_student`) join `tb_course`) join `tb_teacher`) where ((`tb_stucourse`.`StudentNum` = `tb_student`.`StudentNum`) and (`tb_stucourse`.`TeacherNum` = `tb_teacher`.`TeacherNum`) and (`tb_stucourse`.`CourseNum` = `tb_course`.`CourseNum`) and (`tb_stucourse`.`Grade` is not null)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vi_major`
--

/*!50001 DROP VIEW IF EXISTS `vi_major`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vi_major` AS select `tb_major`.`MajorName` AS `MajorName`,`tb_student`.`StudentNum` AS `StudentNum`,`tb_student`.`StudentName` AS `StudentName`,`tb_student`.`StudentSex` AS `StudentSex`,`tb_student`.`StudentBirthday` AS `StudentBirthday` from (`tb_major` join `tb_student`) where (`tb_major`.`MajorNum` = `tb_student`.`MajorNum`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-26 19:04:51
