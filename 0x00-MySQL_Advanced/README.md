# 0x00. MySQL Advanced

## Description

This repository contains solutions to various advanced MySQL tasks aimed at improving and optimizing SQL queries, stored procedures, triggers, and indexing. The tasks are part of the ALX Backend curriculum and focus on leveraging MySQL features for efficient data management and retrieval.

## Table of Contents

1. [Requirements](#requirements)
2. [Concepts](#concepts)
3. [Resources](#resources)
4. [Learning Objectives](#learning-objectives)
5. [Tasks](#tasks)
    - [0. We are all unique!](#0-we-are-all-unique)
    - [1. In and not out](#1-in-and-not-out)
    - [2. Best band ever!](#2-best-band-ever)
    - [3. Old school band](#3-old-school-band)
    - [4. Buy buy buy](#4-buy-buy-buy)
    - [5. Email validation to sent](#5-email-validation-to-sent)
    - [6. Add bonus](#6-add-bonus)
    - [7. Average score](#7-average-score)
    - [8. Optimize simple search](#8-optimize-simple-search)

## Requirements

- Ubuntu 18.04 LTS
- MySQL 5.7 (version 5.7.30)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## Concepts

For this project, the following concepts are relevant:

- Advanced SQL

## Resources

Read or watch:

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## Learning Objectives

By the end of this project, you should be able to explain the following without external help:

- How to create tables with constraints
- How to optimize queries by adding indexes
- What are and how to implement stored procedures and functions in MySQL
- What are and how to implement views in MySQL
- What are and how to implement triggers in MySQL

## Tasks

### 0. We are all unique!
**File:** `0-uniq_users.sql`

Create a table `users` with the following attributes:
- `id`: integer, never null, auto increment, primary key
- `email`: string (255 characters), never null, unique
- `name`: string (255 characters)

### 1. In and not out
**File:** `1-country_users.sql`

Create a table `users` with the following attributes:
- `id`: integer, never null, auto increment, primary key
- `email`: string (255 characters), never null, unique
- `name`: string (255 characters)
- `country`: enumeration of countries: US, CO, and TN, never null (default: US)

### 2. Best band ever!
**File:** `2-fans.sql`

Rank country origins of bands by the number of non-unique fans.
- Import table dump: `metal_bands.sql.zip`
- Columns: `origin` and `nb_fans`

### 3. Old school band
**File:** `3-glam_rock.sql`

List all bands with Glam rock as their main style, ranked by their longevity.
- Import table dump: `metal_bands.sql.zip`
- Columns: `band_name` and `lifespan` (in years until 2022)

### 4. Buy buy buy
**File:** `4-store.sql`

Create a trigger to decrease the quantity of an item after adding a new order.
- Context: Updating multiple tables for one action can generate issues; let MySQL handle it.

### 5. Email validation to sent
**File:** `5-valid_email.sql`

Create a trigger to reset the attribute `valid_email` only when the email has been changed.
- Context: Useful for user email validation.

### 6. Add bonus
**File:** `6-bonus.sql`

Create a stored procedure `AddBonus` to add a new correction for a student.
- Procedure `AddBonus` takes 3 inputs: `user_id`, `project_name`, `score`.

### 7. Average score
**File:** `7-average_score.sql`

Create a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student.
- Procedure `ComputeAverageScoreForUser` takes 1 input: `user_id`.

### 8. Optimize simple search
**File:** `8-index_my_names.sql`

Create an index `idx_name_first` on the table `names` and the first letter of `name`.
- Context: Indexing can greatly improve performance if used correctly.

## Usage

To execute the scripts, ensure MySQL is running, then use the following command format:

```sh
$ mysql -uroot -p < script_name.sql
```

For example, to execute the `0-uniq_users.sql` script:

```sh
$ mysql -uroot -p < 0-uniq_users.sql
```

Replace `script_name.sql` with the name of the script you wish to execute.

---

This project was developed as part of the ALX Backend curriculum to enhance skills in MySQL and advanced SQL concepts.
