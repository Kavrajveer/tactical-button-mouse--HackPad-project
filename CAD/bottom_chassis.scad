// --- TACTICAL HACKPAD BOTTOM CHASSIS ---
// Matches the 80x120mm top plate with internal routing space

$fn = 50;

width = 80;
height = 120;
depth = 15;        // Internal space for wiring and the RP2040
wall = 3;          // 3mm thick walls for durability
floor_thick = 2;   // 2mm solid bottom floor

difference() {
    // 1. The Main Solid Block
    cube([width, height, depth + floor_thick]);

    // 2. Hollow out the inside for electronics
    translate([wall, wall, floor_thick])
        cube([width - (2*wall), height - (2*wall), depth + 1]);

    // 3. USB-C Port Cutout (Top Edge)
    // Centered, allowing plenty of clearance for a standard USB-C cable
    translate([width/2 - 6, height - wall - 1, floor_thick + 4])
        cube([12, wall + 2, 7]);
}

// 4. --- MOUNTING STANDOFFS ---
// Corner posts with 4mm holes to melt the M3 heatset inserts into
module standoff(x, y) {
    translate([x, y, floor_thick])
        difference() {
            cylinder(h=depth, d=8); // The solid post
            cylinder(h=depth+1, d=4); // The hole for the brass insert
        }
}

// Place standoffs in the four corners
standoff(wall + 4, wall + 4);
standoff(width - wall - 4, wall + 4);
standoff(wall + 4, height - wall - 4);
standoff(width - wall - 4, height - wall - 4);
