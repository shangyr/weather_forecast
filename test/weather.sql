/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.1.5
 Source Server Type    : MySQL
 Source Server Version : 50744
 Source Host           : 192.168.1.30:3306
 Source Schema         : weather

 Target Server Type    : MySQL
 Target Server Version : 50744
 File Encoding         : 65001

 Date: 16/12/2024 18:08:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `userId` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`userId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '11111', '2233233');
INSERT INTO `user` VALUES (8, 'aaa', 'aaa');
INSERT INTO `user` VALUES (9, 'eeee', 'eeee');
INSERT INTO `user` VALUES (10, 'qqqq', 'qqqq');
INSERT INTO `user` VALUES (11, '111111', '111111');
INSERT INTO `user` VALUES (12, 'qqq', 'qqq');
INSERT INTO `user` VALUES (13, '1111', '1111');
INSERT INTO `user` VALUES (14, '111', '111');
INSERT INTO `user` VALUES (15, 'tttt', 'tttt');
INSERT INTO `user` VALUES (16, 'iiii', 'iiii');
INSERT INTO `user` VALUES (17, '1111', '1111');

SET FOREIGN_KEY_CHECKS = 1;
