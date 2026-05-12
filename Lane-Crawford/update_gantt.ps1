$csvPath = "LC3.csv"
$outputPath = "LC3_updated.csv"

# Read the CSV file
$csv = Import-Csv -Path $csvPath

# Define Hong Kong public holidays
$holidays = @(
    [datetime]"2026-01-01", # New Year's Day
    [datetime]"2026-01-29", # Chinese New Year
    [datetime]"2026-01-30", # Chinese New Year
    [datetime]"2026-01-31", # Chinese New Year
    [datetime]"2026-04-03", # Good Friday
    [datetime]"2026-04-04", # Holy Saturday
    [datetime]"2026-04-06", # Easter Monday
    [datetime]"2026-04-07", # Ching Ming Festival
    [datetime]"2026-05-01", # Labour Day
    [datetime]"2026-05-25", # Buddha's Birthday
    [datetime]"2026-07-01", # Hong Kong SAR Establishment Day
    [datetime]"2026-09-16", # Mid-Autumn Festival
    [datetime]"2026-10-01"  # National Day
)

# Function to check if a date is a weekend
function Is-Weekend {
    param([datetime]$date)
    return $date.DayOfWeek -eq "Saturday" -or $date.DayOfWeek -eq "Sunday"
}

# Function to check if a date is a holiday
function Is-Holiday {
    param([datetime]$date)
    return $holidays -contains $date.Date
}

# Find project start date (Feb 12, 2026)
$projectStart = [datetime]"2026-02-12"

# Find project end date (latest end date in the CSV)
$projectEnd = $projectStart
foreach ($row in $csv) {
    if ($row."End Date") {
        try {
            $endDate = [datetime]::ParseExact($row."End Date", "M/d/yyyy", $null)
            if ($endDate -gt $projectEnd) {
                $projectEnd = $endDate
            }
        } catch {
            # Skip if date parsing fails
        }
    }
}

# Generate all dates from project start to project end
$allDates = @()
$currentDate = $projectStart
while ($currentDate -le $projectEnd) {
    $allDates += $currentDate
    $currentDate = $currentDate.AddDays(1)
}

# Create new CSV with headers
$newCsv = @()

# Create header row
$headerRow = [ordered]@{
    "Store" = "Store"
    "Section" = "Section"
    "Space (sq ft)" = "Space (sq ft)"
    "Task" = "Task"
    "Start Date" = "Start Date"
    "End Date" = "End Date"
    "Duration (Days)" = "Duration (Days)"
}

# Add date columns to header
foreach ($date in $allDates) {
    $dateStr = $date.ToString("M/d/yyyy")
    $headerRow[$dateStr] = $dateStr
}

# Add total work days column
$headerRow["Total Work Days"] = "Total Work Days"

$newCsv += [PSCustomObject]$headerRow

# Process each row
foreach ($row in $csv) {
    if ($row."Start Date" -and $row."End Date") {
        try {
            $startDate = [datetime]::ParseExact($row."Start Date", "M/d/yyyy", $null)
            $endDate = [datetime]::ParseExact($row."End Date", "M/d/yyyy", $null)
            
            # Calculate duration in days
            $duration = ($endDate - $startDate).Days + 1
            
            # Create new row
            $newRow = [ordered]@{
                "Store" = $row.Store
                "Section" = $row.Section
                "Space (sq ft)" = $row."Space (sq ft)"
                "Task" = $row.Task
                "Start Date" = $row."Start Date"
                "End Date" = $row."End Date"
                "Duration (Days)" = $duration
            }
            
            # Add Gantt chart cells
            $workDays = 0
            foreach ($date in $allDates) {
                $dateStr = $date.ToString("M/d/yyyy")
                if ($date -ge $startDate -and $date -le $endDate) {
                    if ((Is-Weekend -date $date) -or (Is-Holiday -date $date)) {
                        $newRow[$dateStr] = "0"
                    } else {
                        $newRow[$dateStr] = "x"
                        $workDays++
                    }
                } else {
                    $newRow[$dateStr] = ""
                }
            }
            
            # Add total work days
            $newRow["Total Work Days"] = $workDays
            
            $newCsv += [PSCustomObject]$newRow
        } catch {
            # If date parsing fails, just add the original row
            Write-Host "Error processing row: $_"
        }
    }
}

# Export to CSV
$newCsv | Export-Csv -Path $outputPath -NoTypeInformation

Write-Host "Gantt chart created successfully in $outputPath"