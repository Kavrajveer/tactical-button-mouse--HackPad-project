// --- TACTICAL HACKPAD TOP PLATE ---
// Dimensions exactly match 1.5mm mechanical requirements

$fn = 50; // Smooths out the circular holes

plate_width = 80;
plate_height = 120;
thickness = 1.5;

switch_size = 14; 
encoder_radius = 3.5; // 7mm diameter
oled_w = 26;
oled_h = 15;

difference() {
    // 1. The Main Base Plate
    cube([plate_width, plate_height, thickness]);

    // 2. --- TOP SECTION (OLED & Encoders) ---
    // OLED (Center Top)
    translate([plate_width/2 - oled_w/2, plate_height - 25, -1])
        cube([oled_w, oled_h, thickness + 2]);

    // Speed Encoder (Left)
    translate([15, plate_height - 17.5, -1])
        cylinder(h=thickness+2, r=encoder_radius);

    // Scroll Encoder (Right)
    translate([plate_width - 15, plate_height - 17.5, -1])
        cylinder(h=thickness+2, r=encoder_radius);

    // 3. --- BUTTON MATRIX SECTION ---
    cx = plate_width / 2 - switch_size / 2;
    cy = 45;
    spacing = 19.05; // Standard Cherry MX keycap spacing

    // Center Cross
    translate([cx, cy + spacing, -1]) cube([switch_size, switch_size, thickness + 2]); // Up
    translate([cx, cy - spacing, -1]) cube([switch_size, switch_size, thickness + 2]); // Down
    translate([cx - spacing, cy, -1]) cube([switch_size, switch_size, thickness + 2]); // Left
    translate([cx + spacing, cy, -1]) cube([switch_size, switch_size, thickness + 2]); // Right
    translate([cx, cy, -1]) cube([switch_size, switch_size, thickness + 2]); // Single Click (Center)

    // Outer Buttons
    translate([cx - spacing, cy + spacing, -1]) cube([switch_size, switch_size, thickness + 2]); // Double Click (Top Left)
    translate([cx + spacing, cy + spacing, -1]) cube([switch_size, switch_size, thickness + 2]); // Left Click (Top Right)
    translate([cx - spacing, cy - spacing, -1]) cube([switch_size, switch_size, thickness + 2]); // Select (Bottom Left)
}
