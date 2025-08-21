USE Covid19;

select * from dbo.CovidDeaths$ ORDER BY 3,4;

SELECT * FROM dbo.CovidVaccinations$ ORDER BY 3,4;


-- Select Data to use
SELECT location, date, total_cases, new_cases, total_deaths, population
FROM dbo.CovidDeaths$
ORDER BY 1, 2;

-- Total Cases vs Total Deaths
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases) * 100 AS DeathPercentage
FROM dbo.CovidDeaths$
ORDER BY 1, 2;

-- Total Cases vs Total Deaths in Kenya
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases) * 100 AS DeathPercentage
FROM dbo.CovidDeaths$
WHERE location = 'Kenya'
AND continent IS NOT NULL
ORDER BY 1, 2;

-- Looking at Total Cases vs Population
SELECT location, date, population, total_cases, ROUND((total_cases/population) * 100, 4) AS CasesPercentage
FROM dbo.CovidDeaths$
-- WHERE location = 'Kenya'
WHERE continent IS NOT NULL
ORDER BY 1, 2;

-- Countries with Highest Infection Rate compared to Population
SELECT location, population, MAX(total_cases) AS HighestInfectionCount, MAX((total_cases/population)) * 100 AS PercentPopulationInfected
FROM dbo.CovidDeaths$
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY PercentPopulationInfected DESC;


-- Countries with Highest Death count per Population
SELECT location, MAX(CAST(Total_deaths AS INT)) AS TotalDeathCount
FROM dbo.CovidDeaths$
-- WHERE location = 'Kenya'.
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY TotalDeathCount DESC;

-- Exploring by Continent
SELECT location, MAX(CAST(Total_deaths AS INT)) AS TotalDeathCount
FROM dbo.CovidDeaths$
-- WHERE location = 'Kenya'.
WHERE continent IS NULL
GROUP BY location
ORDER BY TotalDeathCount DESC;

--  Continents with the highest death count per population
SELECT continent, MAX(CAST(Total_deaths AS INT)) AS TotalDeathCount
FROM dbo.CovidDeaths$
-- WHERE location = 'Kenya'.
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY TotalDeathCount DESC;

-- Global Numbers
SELECT SUM(new_cases) AS total_cases, SUM(CAST(new_deaths AS INT)) AS total_deaths, SUM(CAST(new_deaths AS INT))/SUM(new_cases) * 100 AS DeathPercentage
FROM dbo.CovidDeaths$
WHERE continent IS NOT NULL;

-- Total population vs Vaccinations

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
    SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingVaccinations
FROM dbo.CovidDeaths$ dea
JOIN dbo.CovidVaccinations$ vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
AND vac.new_vaccinations IS NOT NULL
ORDER BY 2,3;

-- Using CTE
WITH PopvsVac AS (
    SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
        SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingVaccinations
    FROM dbo.CovidDeaths$ dea
    JOIN dbo.CovidVaccinations$ vac
        ON dea.location = vac.location
        AND dea.date = vac.date
    WHERE dea.continent IS NOT NULL
    AND vac.new_vaccinations IS NOT NULL
)

SELECT *, (RollingVaccinations/population) * 100 AS VaccinationPercentage
FROM PopvsVac
ORDER by 2,3;


-- Using Temp table
DROP TABLE IF EXISTS #PercentagePopulationVaccinated
CREATE TABLE #PercentagePopulationVaccinated (
    Continent VARCHAR(100),
    Location VARCHAR(100),
    Date DATE,
    Population NUMERIC,
    New_Vaccinations NUMERIC,
    RollingVaccinations NUMERIC
)

INSERT INTO #PercentagePopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
        SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingVaccinations
    FROM dbo.CovidDeaths$ dea
    JOIN dbo.CovidVaccinations$ vac
        ON dea.location = vac.location
        AND dea.date = vac.date
    WHERE dea.continent IS NOT NULL
    AND vac.new_vaccinations IS NOT NULL

SELECT *, (RollingVaccinations/population) * 100 AS VaccinationPercentage
FROM #PercentagePopulationVaccinated
ORDER by 2,3;

-- Creating view
CREATE VIEW PercentagePopulationVaccinated AS
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
        SUM(CONVERT(INT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingVaccinations
FROM dbo.CovidDeaths$ dea
JOIN dbo.CovidVaccinations$ vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
AND vac.new_vaccinations IS NOT NULL;

SELECT *, (RollingVaccinations/population) * 100 AS VaccinationPercentage
FROM PercentagePopulationVaccinated
ORDER BY 2,3;