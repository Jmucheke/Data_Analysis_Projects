/*

    Cleaning Data using SQL Queries

*/

-- Selecting Database
USE HousingData;

-- Querying the whole table
SELECT * FROM dbo.NashvilleHousing;

-- Querying columns data type
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'NashvilleHousing';

--  Standardize the Date format
SELECT SaleDate, CONVERT(Date, SaleDate)
FROM dbo.NashvilleHousing

-- Method 1: Using CONVERT to change the SaleDate format
UPDATE dbo.NashvilleHousing
SET SaleDate = CONVERT(Date, SaleDate);

-- Mthod 2: creating a new column with the correct date format
ALTER TABLE dbo.NashvilleHousing
ADD SaleDateConverted Date;

UPDATE dbo.NashvilleHousing
SET SaleDateConverted = CONVERT(Date, SaleDate);


-- Querying null values in the Property Address column
SELECT *
FROM dbo.NashvilleHousing
WHERE ParcelID IN (
    SELECT ParcelID
    FROM dbo.NashvilleHousing
    GROUP BY ParcelID
    HAVING COUNT(CASE WHEN PropertyAddress IS NULL THEN 1 END) > 0
        AND COUNT(CASE WHEN PropertyAddress IS NOT NULL THEN 1 END) > 0
)



-- Populating the Property Address Data
SELECT nh.ParcelID, nh.PropertyAddress,nh2.ParcelID, nh2.PropertyAddress, ISNULL(nh.PropertyAddress, nh2.PropertyAddress)
FROM dbo.NashvilleHousing AS nh
JOIN dbo.NashvilleHousing AS nh2
    ON nh.ParcelID = nh2.ParcelID
    AND nh.[UniqueID ] <> nh2.[UniqueID ]
WHERE nh.PropertyAddress IS NULL

-- Updating the Property Address column with the correct values
UPDATE nh
SET nh.PropertyAddress = ISNULL(nh.PropertyAddress, nh2.PropertyAddress)
FROM dbo.NashvilleHousing AS nh
JOIN dbo.NashvilleHousing AS nh2
    ON nh.ParcelID = nh2.ParcelID
    AND nh.[UniqueID ] <> nh2.[UniqueID ]
WHERE nh.PropertyAddress IS NULL;

-- Splitting the Property Address into Address, City

SELECT PropertyAddress
FROM dbo.NashvilleHousing;


SELECT
    SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1) AS Address,
    SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyAddress)) AS City
FROM dbo.NashvilleHousing

ALTER TABLE dbo.NashvilleHousing
ADD PropertyAddressSplit VARCHAR(255),
    PropertyCity VARCHAR(255)

UPDATE dbo.NashvilleHousing
SET PropertyAddressSplit = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1),
    PropertyCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1, LEN(PropertyAddress))

-- Querying the updated table
SELECT *
FROM dbo.NashvilleHousing;

-- Droppimg the old columns
ALTER TABLE dbo.NashvilleHousing
DROP COLUMN Address, City;

-- Splitting the Owner Address into Address, City, State
SELECT
    PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3) AS Address,
    PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2) AS City,
    PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1) AS State
FROM dbo.NashvilleHousing;


ALTER TABLE dbo.NashvilleHousing
ADD OwnerAddressSplit VARCHAR(255),
    OwnerCity VARCHAR(255),
    OwnerState VARCHAR(255);

UPDATE dbo.NashvilleHousing
SET OwnerAddressSplit = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3),
    OwnerCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2),
    OwnerState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1);

-- Change Y and N to Yes and No in SoldAsVacant column
SELECT DISTINCT SoldAsVacant, COUNT(SoldAsVacant)
FROM dbo.NashvilleHousing
GROUP BY SoldAsVacant;

SELECT 
    CASE
        WHEN SoldAsVacant = 'y' THEN 'Yes'
        WHEN SoldAsVacant = 'N' THEN 'No'
        ELSE SoldAsVacant
    END AS SoldAsVacant
FROM dbo.NashvilleHousing;

UPDATE dbo.NashvilleHousing
SET SoldAsVacant = 
    CASE
        WHEN SoldAsVacant = 'y' THEN 'Yes'
        WHEN SoldAsVacant = 'N' THEN 'No'
        ELSE SoldAsVacant
    END

-- Removing duplicates

WITH RowNUMcte AS (
SELECT *,
    ROW_NUMBER() OVER (
        PARTITION BY ParcelID, PropertyAddress,SalePrice,SaleDate,LegalReference ORDER BY [UniqueID]
    ) row_num

FROM dbo.NashvilleHousing
)

DELETE 
FROM RowNUMcte
WHERE row_num > 1;

-- Deleting Unused duplicates
ALTER TABLE dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress;
