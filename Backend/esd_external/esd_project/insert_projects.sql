-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Mar 30, 2024 at 07:24 AM
-- Server version: 5.7.39
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

DROP DATABASE IF EXISTS `project`;
CREATE DATABASE IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `project`;

-- --------------------------------------------------------

--
-- Table structure for table `project`
--


CREATE TABLE `project` (
  `proj_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `proj_name` text NOT NULL,
  `proj_image` text NOT NULL,
  `proj_description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`proj_id`, `user_id`, `proj_name`, `proj_image`, `proj_description`) VALUES
(43, 100, 'YouTube Channel Launch: Eco-Friendly Living', 'proj1.jpg', 'Creating engaging videos promoting sustainable lifestyle choices for viewers.'),
(44, 100, 'Instagram Campaign: Reduce, Reuse, Recycle', 'proj2.jpg', 'Launching an Instagram campaign to inspire followers to adopt eco-friendly practices.'),
(45, 100, 'Podcast Series: Green Living Discussions', 'proj3.jpg', 'Starting a podcast series discussing topics related to environmental conservation and green living.'),
(46, 100, 'Blog: Sustainable Fashion Trends', 'proj4.jpg', 'Writing blog posts showcasing sustainable fashion brands and trends for conscious consumers.'),
(47, 100, 'Ebook: Beginner Guide to Zero Waste Living', 'proj5.jpg', 'Writing an ebook providing tips and resources for transitioning to a zero waste lifestyle.'),
(48, 100, 'YouTube Series: Healthy Cooking Made Easy', 'proj6.jpg', 'Creating cooking tutorials focusing on easy and nutritious recipes for health-conscious viewers.'),
(49, 100, 'TikTok Channel: Fitness Challenges', 'proj7.jpg', 'Starting a TikTok channel featuring fun fitness challenges to inspire followers to stay active.'),
(50, 100, 'Instagram Reels: Wellness Tips', 'proj8.jpg', 'Sharing short wellness tips and self-care routines through Instagram Reels to promote mental health.'),
(51, 100, 'Podcast: Mindfulness Meditation Sessions', 'proj9.jpg', 'Hosting guided meditation sessions on a podcast platform to help listeners cultivate mindfulness.'),
(52, 100, 'Blog: Healthy Lifestyle Inspirations', 'proj10.jpg', 'Curating blog content featuring stories and inspirations from individuals who have adopted a healthy lifestyle.'),
(53, 100, 'YouTube Vlogs: Urban Gardening Adventures', 'proj11.jpg', 'Documenting the journey of creating and maintaining urban gardens through engaging vlogs.'),
(54, 100, 'Instagram Reels: DIY Home Decor Ideas', 'proj12.jpg', 'Sharing creative DIY home decor projects and ideas through short and engaging Instagram Reels.'),
(55, 100, 'Podcast: Sustainable Living Interviews', 'proj13.jpg', 'Conducting interviews with experts and influencers in the sustainable living space for a podcast series.'),
(56, 100, 'Blog: Eco-Friendly Travel Guides', 'proj14.jpg', 'Writing travel guides highlighting eco-friendly destinations, accommodations, and activities for eco-conscious travelers.'),
(57, 125, 'Ebook: Plant-Based Recipes Cookbook', 'proj15.jpg', 'Compiling a collection of plant-based recipes into an ebook to encourage more people to adopt a plant-based diet.'),
(58, 126, 'YouTube Channel: Tech Reviews and Tutorials', 'proj16.jpg', 'Creating tech review videos and tutorials to help viewers make informed decisions about gadgets and devices.'),
(59, 126, 'Twitch Streaming: Gaming and Tech Discussions', 'proj17.jpg', 'Streaming live discussions on Twitch about gaming, tech news, and industry trends to engage with the community.'),
(60, 126, 'Instagram Live: Coding Workshops', 'proj18.jpg', 'Hosting live coding workshops on Instagram to teach coding basics and advanced techniques to aspiring developers.'),
(61, 126, 'Podcast: Future Tech Trends Analysis', 'proj19.jpg', 'Analyzing and discussing emerging technology trends and innovations in a podcast series for tech enthusiasts.'),
(62, 126, 'Blog: Tech Productivity Hacks and Tips', 'proj20.jpg', 'Sharing productivity hacks and tips for maximizing efficiency in tech-related tasks through blog posts.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`proj_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `proj_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
