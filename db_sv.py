import MySQLdb

db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()

sql = """-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.21-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for sinhviendb
CREATE DATABASE IF NOT EXISTS `sinhviendb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `sinhviendb`;

-- Dumping structure for table sinhviendb.khoa
CREATE TABLE IF NOT EXISTS `khoa` (
  `Makhoa` varchar(255) NOT NULL,
  `TenKhoa` varchar(255) NOT NULL,
  PRIMARY KEY (`Makhoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table sinhviendb.khoa: ~0 rows (approximately)
DELETE FROM `khoa`;
/*!40000 ALTER TABLE `khoa` DISABLE KEYS */;
/*!40000 ALTER TABLE `khoa` ENABLE KEYS */;

-- Dumping structure for table sinhviendb.lop
CREATE TABLE IF NOT EXISTS `lop` (
  `MALOP` varchar(255) NOT NULL,
  `MAKHOA` varchar(255) NOT NULL,
  `TENLOP` varchar(255) DEFAULT NULL,
  `NIENKHOA` varchar(255) DEFAULT NULL,
  `THOIHAN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`MALOP`),
  UNIQUE KEY `LOP_PK` (`MALOP`),
  KEY `RELATIONSHIP_1_FK` (`MAKHOA`),
  CONSTRAINT `lop_ibfk_1` FOREIGN KEY (`MAKHOA`) REFERENCES `khoa` (`Makhoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table sinhviendb.lop: ~0 rows (approximately)
DELETE FROM `lop`;
/*!40000 ALTER TABLE `lop` DISABLE KEYS */;
/*!40000 ALTER TABLE `lop` ENABLE KEYS */;

-- Dumping structure for table sinhviendb.sinhvien
CREATE TABLE IF NOT EXISTS `sinhvien` (
  `MASV` varchar(255) NOT NULL,
  `MALOP` varchar(255) NOT NULL,
  `HOTEN` varchar(255) NOT NULL,
  `NGAYSINH` varchar(255) NOT NULL,
  `GIOITINH` tinyint(1) NOT NULL,
  `DIACHI` varchar(255) NOT NULL,
  `SDT` int(11) NOT NULL,
  `DIEMTB` float NOT NULL,
  PRIMARY KEY (`MASV`),
  KEY `MALOP` (`MALOP`),
  CONSTRAINT `sinhvien_ibfk_1` FOREIGN KEY (`MALOP`) REFERENCES `lop` (`MALOP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table sinhviendb.sinhvien: ~0 rows (approximately)
DELETE FROM `sinhvien`;
/*!40000 ALTER TABLE `sinhvien` DISABLE KEYS */;
/*!40000 ALTER TABLE `sinhvien` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

"""
try:
      cursor.execute(sql)
      print 'Tao Database thanh cong!'
except TypeError as e:
      print (e)
      db.rollback()
db.close()
