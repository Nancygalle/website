-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 17, 2025 at 06:40 AM
-- Server version: 5.5.20
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pythonproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE IF NOT EXISTS `courses` (
  `ccode` int(11) NOT NULL,
  `cname` varchar(20) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `fees` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`ccode`, `cname`, `duration`, `fees`) VALUES
(102, 'HTML', '1 month', 10000),
(105, 'MS office', '3 months', 20000),
(106, 'MYSQL', '1 month', 12000);

-- --------------------------------------------------------

--
-- Table structure for table `fees`
--

CREATE TABLE IF NOT EXISTS `fees` (
  `Recpno` int(11) NOT NULL,
  `Rdate` date NOT NULL,
  `Adno` int(11) NOT NULL,
  `Balamt` int(11) NOT NULL,
  `Amtpaid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fees`
--

INSERT INTO `fees` (`Recpno`, `Rdate`, `Adno`, `Balamt`, `Amtpaid`) VALUES
(101, '2024-12-02', 1005, 1000, 1000),
(102, '2024-12-11', 1002, 10000, 10000),
(103, '2024-12-11', 1003, 10000, 10000);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `Userid` varchar(30) NOT NULL,
  `Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Userid`, `Password`) VALUES
('admin', 'nancy');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `Adno` int(11) NOT NULL,
  `Addate` datetime NOT NULL,
  `Studentname` varchar(20) NOT NULL,
  `Fathername` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `city` varchar(20) NOT NULL,
  `cname` varchar(20) NOT NULL,
  `Duration` varchar(20) NOT NULL,
  `fee` int(11) NOT NULL,
  `Amtpaid` int(11) NOT NULL,
  `balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Adno`, `Addate`, `Studentname`, `Fathername`, `age`, `gender`, `city`, `cname`, `Duration`, `fee`, `Amtpaid`, `balance`) VALUES
(1002, '2024-12-05 00:00:00', 'Raman', 'Ashok kumar', 26, 'Male', 'Fatehabad', 'android', '', 20000, 10000, 10000),
(1003, '2024-12-05 00:00:00', 'Neha', 'Arun kumar', 30, 'Female', 'Hisar', 'android', '5 months', 20000, 10000, 0),
(1004, '2024-12-05 00:00:00', 'Sukhpreet singh', 'Jagjeet singh', 20, 'Male', 'Fatehabad', 'HTML', '1 month', 10000, 6000, 4000),
(1005, '2024-12-13 00:00:00', 'Manisha', 'Amit kumar', 24, 'Male', 'Delhi', 'PHP', '3 months', 20000, 12000, 8000),
(1006, '2024-12-13 00:00:00', 'Kawaljeet kaur', 'Jagjeet singh', 24, 'Female', 'Fatehabad', 'HTML', '1 month', 10000, 10000, 0),
(1007, '2024-12-13 00:00:00', 'Amanpreet singh', 'Harjinder singh', 28, 'Male', 'Delhi', 'Core java', '3 months', 12000, 9000, 3000),
(1009, '2024-12-13 00:00:00', 'Ravina', 'Arman kumar', 24, 'Female', 'Fatehabad', 'PHP', '3 months', 20000, 10000, 10000),
(1010, '2024-12-13 00:00:00', 'Rahul', 'Parveen kumar', 25, 'Male', 'Sirsa', 'HTML', '1 month', 10000, 10000, 0),
(1011, '2024-12-17 00:00:00', 'ankit', 'himanshu', 21, 'Male', 'Sirsa', 'HTML', '1 month', 10000, 6000, 4000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
