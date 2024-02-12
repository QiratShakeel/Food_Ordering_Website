-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2024 at 02:32 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `food_website_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_app_food_category`
--

CREATE TABLE `admin_app_food_category` (
  `food_cat_id` int(11) NOT NULL,
  `food_cat` varchar(30) NOT NULL,
  `food_type_fk_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_app_food_category`
--

INSERT INTO `admin_app_food_category` (`food_cat_id`, `food_cat`, `food_type_fk_id`) VALUES
(1, 'Beef Mutton', 2),
(2, 'Salad', 3);

-- --------------------------------------------------------

--
-- Table structure for table `admin_app_food_type`
--

CREATE TABLE `admin_app_food_type` (
  `food_id` int(11) NOT NULL,
  `food_type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_app_food_type`
--

INSERT INTO `admin_app_food_type` (`food_id`, `food_type`) VALUES
(2, 'non_veg'),
(3, 'veg');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add food_ type', 7, 'add_food_type'),
(26, 'Can change food_ type', 7, 'change_food_type'),
(27, 'Can delete food_ type', 7, 'delete_food_type'),
(28, 'Can view food_ type', 7, 'view_food_type'),
(29, 'Can add food_ category', 8, 'add_food_category'),
(30, 'Can change food_ category', 8, 'change_food_category'),
(31, 'Can delete food_ category', 8, 'delete_food_category'),
(32, 'Can view food_ category', 8, 'view_food_category'),
(33, 'Can add restaurant', 9, 'add_restaurant'),
(34, 'Can change restaurant', 9, 'change_restaurant'),
(35, 'Can delete restaurant', 9, 'delete_restaurant'),
(36, 'Can view restaurant', 9, 'view_restaurant'),
(37, 'Can add branch', 10, 'add_branch'),
(38, 'Can change branch', 10, 'change_branch'),
(39, 'Can delete branch', 10, 'delete_branch'),
(40, 'Can view branch', 10, 'view_branch'),
(41, 'Can add food_ item', 11, 'add_food_item'),
(42, 'Can change food_ item', 11, 'change_food_item'),
(43, 'Can delete food_ item', 11, 'delete_food_item'),
(44, 'Can view food_ item', 11, 'view_food_item');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$r4uSiYFJr7gixZDfPKFLDB$+htn5XWpV9hYLJesk3juZlLdiVAu6TPP/WE4nDE9FXY=', '2024-02-12 07:14:51.718025', 0, 'zosevy@mailinator.com', '', '', 'sywicyvaj@mailinator.com', 0, 1, '2024-02-11 14:23:39.057292'),
(2, 'pbkdf2_sha256$720000$TVI0PNV2NmC8cUKYK03txd$nxkTEmWBMxapibWZn2RAepq8jnD40WPG7nzipIF2XGI=', '2024-02-12 07:01:49.228066', 1, 'qiratshakeel', '', '', '', 1, 1, '2024-02-11 15:27:15.876975');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(8, 'Admin_App', 'food_category'),
(7, 'Admin_App', 'food_type'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'Restaurant_App', 'branch'),
(11, 'Restaurant_App', 'food_item'),
(9, 'Restaurant_App', 'restaurant'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-09 13:42:03.331656'),
(2, 'auth', '0001_initial', '2024-02-09 13:42:03.687685'),
(3, 'admin', '0001_initial', '2024-02-09 13:42:03.785534'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-09 13:42:03.793535'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-09 13:42:03.802653'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-09 13:42:03.886607'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-09 13:42:03.929285'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-09 13:42:03.942711'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-09 13:42:03.949710'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-09 13:42:04.004011'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-09 13:42:04.006009'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-09 13:42:04.013008'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-09 13:42:04.027185'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-09 13:42:04.041420'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-09 13:42:04.055466'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-09 13:42:04.063464'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-09 13:42:04.075816'),
(18, 'sessions', '0001_initial', '2024-02-09 13:42:04.105908'),
(19, 'Admin_App', '0001_initial', '2024-02-09 13:42:46.749017'),
(20, 'Admin_App', '0002_alter_food_type_food_type', '2024-02-10 13:21:23.113304'),
(21, 'Admin_App', '0003_food_category', '2024-02-10 18:57:46.063234'),
(22, 'Restaurant_App', '0001_initial', '2024-02-11 09:18:23.614783');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1qam6o3fqlorsl1ekp2l0x73ujosbfct', '.eJxVjEEOwiAQRe_C2hAodAZcuvcMhIFBqoYmpV0Z765NutDtf-_9lwhxW2vYOi9hyuIstDj9bhTTg9sO8j222yzT3NZlIrkr8qBdXufMz8vh_h3U2Ou39qTAaQdxSA6QE-ZCNCZrldE-JyAiNGQ8OBx5KLqYyFoxAaMnY1G8P-bFOA8:1rZQWh:4OdNcybJQuxurmQzjvnBvAhrzAa-fiti_AYG-ropceQ', '2024-02-26 07:14:51.720024');

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_app_branch`
--

CREATE TABLE `restaurant_app_branch` (
  `branch_id` int(11) NOT NULL,
  `branch_country` varchar(50) NOT NULL,
  `branch_city` varchar(50) NOT NULL,
  `branch_locality` varchar(50) NOT NULL,
  `rest_fk_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_app_food_item`
--

CREATE TABLE `restaurant_app_food_item` (
  `food_item_id` int(11) NOT NULL,
  `food_item_name` varchar(50) NOT NULL,
  `food_item_desc` varchar(150) NOT NULL,
  `food_item_price` double NOT NULL,
  `food_item_avaliblity` tinyint(1) NOT NULL,
  `food_img` varchar(100) NOT NULL,
  `food_cat_fk_id` int(11) NOT NULL,
  `rest_fk_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_app_restaurant`
--

CREATE TABLE `restaurant_app_restaurant` (
  `rest_id` int(11) NOT NULL,
  `rest_name` varchar(50) NOT NULL,
  `rest_owner_name` varchar(50) NOT NULL,
  `rest_email` varchar(50) NOT NULL,
  `rest_pass` varchar(50) NOT NULL,
  `rest_logo_img` varchar(100) NOT NULL,
  `rest_banner_img` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_app_food_category`
--
ALTER TABLE `admin_app_food_category`
  ADD PRIMARY KEY (`food_cat_id`),
  ADD KEY `Admin_App_food_categ_food_type_fk_id_6cd90b8f_fk_Admin_App` (`food_type_fk_id`);

--
-- Indexes for table `admin_app_food_type`
--
ALTER TABLE `admin_app_food_type`
  ADD PRIMARY KEY (`food_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `restaurant_app_branch`
--
ALTER TABLE `restaurant_app_branch`
  ADD PRIMARY KEY (`branch_id`),
  ADD KEY `Restaurant_App_branc_rest_fk_id_id_aeb51166_fk_Restauran` (`rest_fk_id_id`);

--
-- Indexes for table `restaurant_app_food_item`
--
ALTER TABLE `restaurant_app_food_item`
  ADD PRIMARY KEY (`food_item_id`),
  ADD KEY `Restaurant_App_food__food_cat_fk_id_cd37ec7e_fk_Admin_App` (`food_cat_fk_id`),
  ADD KEY `Restaurant_App_food__rest_fk_id_id_9ff09dd6_fk_Restauran` (`rest_fk_id_id`);

--
-- Indexes for table `restaurant_app_restaurant`
--
ALTER TABLE `restaurant_app_restaurant`
  ADD PRIMARY KEY (`rest_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_app_food_category`
--
ALTER TABLE `admin_app_food_category`
  MODIFY `food_cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `admin_app_food_type`
--
ALTER TABLE `admin_app_food_type`
  MODIFY `food_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `restaurant_app_branch`
--
ALTER TABLE `restaurant_app_branch`
  MODIFY `branch_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `restaurant_app_food_item`
--
ALTER TABLE `restaurant_app_food_item`
  MODIFY `food_item_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `restaurant_app_restaurant`
--
ALTER TABLE `restaurant_app_restaurant`
  MODIFY `rest_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_app_food_category`
--
ALTER TABLE `admin_app_food_category`
  ADD CONSTRAINT `Admin_App_food_categ_food_type_fk_id_6cd90b8f_fk_Admin_App` FOREIGN KEY (`food_type_fk_id`) REFERENCES `admin_app_food_type` (`food_id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `restaurant_app_branch`
--
ALTER TABLE `restaurant_app_branch`
  ADD CONSTRAINT `Restaurant_App_branc_rest_fk_id_id_aeb51166_fk_Restauran` FOREIGN KEY (`rest_fk_id_id`) REFERENCES `restaurant_app_restaurant` (`rest_id`);

--
-- Constraints for table `restaurant_app_food_item`
--
ALTER TABLE `restaurant_app_food_item`
  ADD CONSTRAINT `Restaurant_App_food__food_cat_fk_id_cd37ec7e_fk_Admin_App` FOREIGN KEY (`food_cat_fk_id`) REFERENCES `admin_app_food_category` (`food_cat_id`),
  ADD CONSTRAINT `Restaurant_App_food__rest_fk_id_id_9ff09dd6_fk_Restauran` FOREIGN KEY (`rest_fk_id_id`) REFERENCES `restaurant_app_restaurant` (`rest_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
