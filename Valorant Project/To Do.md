# Re Making Valorant Machine Learning Classification Project 

## To Do / What is Being Developed 

1. Set Up Env For GPU Training Using PyTorch (YoloV8)
2. Get Images for Maps 

    A. Bind
    
    B. Haven
   
    C. Split

    D. Ascent - maps/raw/ascent_raw.png

    E. IceBox

    F. Breeze

    G. Fracture

    H. Pearl

    I. Lotus

    J. Sunset

    K. Abyss

    L. Corrode
3. Get Agent MiniMap Icon: Brimestone, Viper, Omen, Killjoy, Cypher, Sova, Sage, Phoenix, Jett, Reyna, Raze, Breach, Skye, Yoru, Astra, Kayo, Chamber, Neon, Fade, Harbor, Gekko, Deadlock, Iso, Clove, Vyse, Tejo, Waylay, Veto

4. Using the Maps - Create a Bounding Box Limitation for Where Icons can be placed, Go Into a tool and make a White Vs Black Coloring for (White - Can Walk, Black - Cannot Walk)

5. Verify Pixel Count for Icons (14 Pixels or More for Icons)

6. Generate the Syntehtic Dataset

7. Train the ML Model 

8. Verify This works on Real Data 

9. After Verifying this Test to see if we can get the icon Locations