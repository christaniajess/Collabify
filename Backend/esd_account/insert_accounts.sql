CREATE DATABASE IF NOT EXISTS `account` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `account`;
CREATE TABLE IF NOT EXISTS `account` (
  `user_id` INT(10) UNSIGNED NOT NULL,
  `username` TEXT NOT NULL,
  `acc_type` TEXT NOT NULL,
  `full_name` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  `password` TEXT NOT NULL,  -- Consider using a larger length for passwords
  `user_photo` TEXT DEFAULT NULL,
  `interests` TEXT DEFAULT NULL, -- Modified column for user interests
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Insert sample data
INSERT INTO `account` (`user_id`, `username`, `acc_type`, `full_name`, `email`, `password`, `user_photo`, `interests`) VALUES
(1234567890, 'CannotSeeMe', 'cc', 'John Cena', '1915408967@qq.com', 'iLoveWrestling', NULL, 'wrestling,acting');
COMMIT;
