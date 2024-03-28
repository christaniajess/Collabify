DROP DATABASE IF EXISTS `account`;
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
  `stripe_key` TEXT DEFAULT NULL, -- New column for stripe key
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Insert sample data
INSERT INTO `account` (`user_id`, `username`, `acc_type`, `full_name`, `email`, `password`, `user_photo`, `interests`,`stripe_key`) VALUES
                      (1234567890, 'CannotSeeMe', 'cc', 'John Cena', '1915408967@qq.com', 'iLoveWrestling', NULL, 'wrestling,acting','sk_test_51OuGi52KwIS1b45LvlM5Q8z0AaTmdNohKDWk3pOEKhNbvOmHJmCEU9DWbSab871Yal3Qw5H2QMXDynjOuQC6NLXB00NBUhtZne');
COMMIT;
