# UOAF Kuwait Theater

The Kuwait theater campaign modified to create an evocation of the 1991 Gulf War.

# Installation

1. Extract the contents of this zipfile into `<falcon>\Data\` where `<falcon>` is the base directory of your BMS install.
1. When this is done you should have 
1. Open `<falcon>\Data\Terrdata\theaterdefinition\theater.lst`
1. Add the line to the bottom of the list:

```Add-On Kuwait UOAF\Terrdata\theaterdefinition\kuwait.tdf```

5. Save the text file, start Falcon4 BMS 4, select "Kuwait Theater UOAF" from the list of available theaters.
6. Restart BMS.

# Credits and thanks
Thanks to SpbGoro and the Kuwait contributors for their gracious permission for UOAF to build on their hard work.

# Update Tacview to View Kuwait UOAF ACMIs

1. Edit C:\Program Files (x86)\Tacview\Data\Xml\Data-Falcon4Theaters.xml
1. Add this code to the ```<Falcon4Theaters>``` element: 
```
        <Theater ID="Kuwait">
            <Terrain>Data/Add-On Kuwait UOAF/Terrdata/terrain</Terrain>
            <Database>Data/Add-On Kuwait UOAF/Terrdata/Objects</Database>

            <LOD>2</LOD>
            <West>42.0325</West>
            <East>52.3625</East>
            <South>25.10</South>
            <North>34.31</North>
            <Visible>1</Visible>
            <TimeZone>+3</TimeZone>
            <LargeTextureIndex>true</LargeTextureIndex>
        </Theater>
 ```
