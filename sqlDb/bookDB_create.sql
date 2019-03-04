# ---------------------------------------------------------------------- #
# Add tables                                                             #
# ---------------------------------------------------------------------- #

# ---------------------------------------------------------------------- #
# Add table "Author"                                                     #
# ---------------------------------------------------------------------- #

CREATE TABLE `Author` (
    `AuthorId` INTEGER NOT NULL AUTO_INCREMENT,
    `FirstName` VARCHAR(40) NOT NULL,
    `LastName` VARCHAR(40) NOT NULL,
    CONSTRAINT `PK_Author` PRIMARY KEY (`AuthorId`)
);

# ---------------------------------------------------------------------- #
# Add table "Category"                                                   #
# ---------------------------------------------------------------------- #

CREATE TABLE `Category` (
    `CategoryId` INTEGER NOT NULL AUTO_INCREMENT,
    `Name` VARCHAR(255) NOT NULL,
    CONSTRAINT `PK_Category` PRIMARY KEY (`CategoryId`)
);

# ---------------------------------------------------------------------- #
# Add table "Publisher"                                                  #
# ---------------------------------------------------------------------- #

CREATE TABLE `Publisher` (
    `PublisherId` INTEGER NOT NULL AUTO_INCREMENT,
    `Name` VARCHAR(255) NOT NULL,
    CONSTRAINT `PK_Publisher` PRIMARY KEY (`PublisherId`)
);

# ---------------------------------------------------------------------- #
# Add table "User"                                                       #
# ---------------------------------------------------------------------- #

CREATE TABLE `User` (
    `UserId` INTEGER NOT NULL AUTO_INCREMENT,
    `FirstName` VARCHAR(40),
    `userName` VARCHAR(40) NOT NULL,
    `password` VARCHAR(8) NOT NULL,
    CONSTRAINT `PK_User` PRIMARY KEY (`UserId`)
);

# ---------------------------------------------------------------------- #
# Add table "ReadingList"                                                #
# ---------------------------------------------------------------------- #

CREATE TABLE `ReadingList` (
    `ListId` INTEGER NOT NULL AUTO_INCREMENT,
    `UserId` INTEGER NOT NULL,
    `ListName` VARCHAR(255) NOT NULL,
    CONSTRAINT `PK_ReadingList` PRIMARY KEY (`ListId`)
);

# ---------------------------------------------------------------------- #
# Add table "Book"                                                       #
# ---------------------------------------------------------------------- #

CREATE TABLE `Book` (
    `isbn` INTEGER NOT NULL AUTO_INCREMENT,
    `Title` VARCHAR(255) NOT NULL,
    `PublisherId` INTEGER NOT NULL,
    `Year` YEAR NOT NULL,
    `CategoryId` INTEGER NOT NULL,
    `BookCover` VARCHAR(255),
    CONSTRAINT `PK_Book` PRIMARY KEY (`isbn`)
);

# ---------------------------------------------------------------------- #
# Add table "Author_book"                                                #
# ---------------------------------------------------------------------- #

CREATE TABLE `Author_book` (
    `AuthorId` INTEGER NOT NULL,
    `isbn` INTEGER NOT NULL
);

# ---------------------------------------------------------------------- #
# Add table "Book_readingList"                                           #
# ---------------------------------------------------------------------- #

CREATE TABLE `Book_readingList` (
    `isbn` INTEGER NOT NULL,
    `ListId` INTEGER NOT NULL
);

# ---------------------------------------------------------------------- #
# Add foreign key constraints                                            #
# ---------------------------------------------------------------------- #

ALTER TABLE `Book` ADD CONSTRAINT `Publisher_Book` 
    FOREIGN KEY (`PublisherId`) REFERENCES `Publisher` (`PublisherId`);

ALTER TABLE `Book` ADD CONSTRAINT `Category_Book` 
    FOREIGN KEY (`CategoryId`) REFERENCES `Category` (`CategoryId`);

ALTER TABLE `ReadingList` ADD CONSTRAINT `User_ReadingList` 
    FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`);

ALTER TABLE `Author_book` ADD CONSTRAINT `Author_Author_book` 
    FOREIGN KEY (`AuthorId`) REFERENCES `Author` (`AuthorId`);

ALTER TABLE `Author_book` ADD CONSTRAINT `Book_Author_book` 
    FOREIGN KEY (`isbn`) REFERENCES `Book` (`isbn`);

ALTER TABLE `Book_readingList` ADD CONSTRAINT `ReadingList_Book_readingList` 
    FOREIGN KEY (`ListId`) REFERENCES `ReadingList` (`ListId`);

ALTER TABLE `Book_readingList` ADD CONSTRAINT `Book_Book_readingList` 
    FOREIGN KEY (`isbn`) REFERENCES `Book` (`isbn`);
