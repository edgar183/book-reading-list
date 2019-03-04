# ---------------------------------------------------------------------- #
# Drop foreign key constraints                                           #
# ---------------------------------------------------------------------- #

ALTER TABLE `Book` DROP FOREIGN KEY `Publisher_Book`;

ALTER TABLE `Book` DROP FOREIGN KEY `Category_Book`;

ALTER TABLE `ReadingList` DROP FOREIGN KEY `User_ReadingList`;

ALTER TABLE `Author_book` DROP FOREIGN KEY `Author_Author_book`;

ALTER TABLE `Author_book` DROP FOREIGN KEY `Book_Author_book`;

ALTER TABLE `Book_readingList` DROP FOREIGN KEY `ReadingList_Book_readingList`;

ALTER TABLE `Book_readingList` DROP FOREIGN KEY `Book_Book_readingList`;

# ---------------------------------------------------------------------- #
# Drop table "Book_readingList"                                          #
# ---------------------------------------------------------------------- #

# Drop constraints #

DROP TABLE `Book_readingList`;

# ---------------------------------------------------------------------- #
# Drop table "Author_book"                                               #
# ---------------------------------------------------------------------- #

# Drop constraints #

DROP TABLE `Author_book`;

# ---------------------------------------------------------------------- #
# Drop table "Book"                                                      #
# ---------------------------------------------------------------------- #

# Drop constraints #

ALTER TABLE `Book` DROP PRIMARY KEY;

DROP TABLE `Book`;

# ---------------------------------------------------------------------- #
# Drop table "ReadingList"                                               #
# ---------------------------------------------------------------------- #

# Drop constraints #

ALTER TABLE `ReadingList` DROP PRIMARY KEY;

DROP TABLE `ReadingList`;

# ---------------------------------------------------------------------- #
# Drop table "User"                                                      #
# ---------------------------------------------------------------------- #

# Drop constraints #

ALTER TABLE `User` DROP PRIMARY KEY;

DROP TABLE `User`;

# ---------------------------------------------------------------------- #
# Drop table "Publisher"                                                 #
# ---------------------------------------------------------------------- #

# Drop constraints #

ALTER TABLE `Publisher` DROP PRIMARY KEY;

DROP TABLE `Publisher`;

# ---------------------------------------------------------------------- #
# Drop table "Category"                                                  #
# ---------------------------------------------------------------------- #

# Drop constraints #

ALTER TABLE `Category` DROP PRIMARY KEY;

DROP TABLE `Category`;

# ---------------------------------------------------------------------- #
# Drop table "Author"                                                    #
# ---------------------------------------------------------------------- #

# Drop constraints #

ALTER TABLE `Author` DROP PRIMARY KEY;

DROP TABLE `Author`;
