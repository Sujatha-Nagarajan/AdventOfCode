import re
from collections import defaultdict

input1="""sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

input2="""nwesesesesewswenwswsesesenesenwnesenwse
nwnenwnwnenenwnenwnenewnwenenwwnenesesenw
neneswnenwenwseeneweswsenesewnenenee
senwewnwnenenwnwnwwesenenwswnenwwnwnw
swseseeseswseseeswseneseswsesesenwsesew
weeneeneswsewnwnesweseneswenwneswne
swseseswswneswswsesewswswseswse
swswseeswswwswnweenewswswesenwswwse
swswswswsweswseeswseseseseeswwsewnw
eneeseenenweeneenenee
eesesenwsesweeseeese
neenenenewnenenenenenwnenenenwnwne
nenenwnwnwnenwnenwnwswnenesenenwnw
neneweweneneenenenenesewneeneenee
nwweswswewneenenwneneneeswneneneswne
eeseeneseesesesewneswseeeseese
swseswsenwswnewswseswswswseswswse
senenenwnwnenwnwnwewnwwnwswnenenwnwnwenw
senwnenenwnwnenwnwwnwswnwnwnenwnwenenwnw
neweseneswswnwswnwswseneseenwseeswee
esesweeneeneswsenwsweeeeseeseee
nenenwewseswseseswsewseneewwwnww
neeswswenwnewnwnwwswwwneswswnwwwnwnw
wwweswwwwwwswwwwww
eeseenweenwseneeeeeeweeenee
eeeeesenenenwesweeeswenwswseswee
neswenenesenenenewnwenesweneneeswne
swswswenwswwswswswswswwwswweswnwsww
seseswseseseeswneeeeesewesesenenw
swwswwwswwwswwswsweneswwwsesww
eneeswenweewenwseeeseeeseswwnw
swnenwswswswseseswswswwseswswswswswswsw
seeseseeseeeesesesenwsenwseweseese
swswswswnwnesweswewseseneswswwnenwsw
eewnenweneswwseeeeneneeeeeene
esenweswwnwnwnwnwnwnwnwnwnwnwnwnwwnw
seeeeeseeneeswweeeeeeneenw
weneswswenenenenwneswneswneneneesene
wnwsesesenwnwnenwnwnesweneenwseswwsw
sewsesesesesesesesewsenesesesesesenesese
swswswwnwswswwweswswswnewwseswsww
nwneneswnwnwnenenenwsenenwnwnenwwnene
neenwenenwsweseeswsesweeseseswneswene
eneeenewewneeneeneweneeesee
nwnwwwnwnewsenwsenw
sesesewswswwneneneeseeewswnwswnwsenw
sewwswwnwwewwwneswswswwwneew
nwsenwwnenenenesenwsenenenenenenenenenwne
sewsewnesenwsenesenwsesweswswsesenenw
eseeeeeeeenweeeeseesee
eseenwseesweswenweseenweeeeswee
neseseseswwneswsesesesewseseseswse
sesweewseseeesenwseeeseeswsweneenw
wnwneseeeseseeseenwwenwseseesese
enwneswnwneneneneneneneenenwnenwwnene
wnwneneneneneneewnwwnenweneesw
nwnenenenwnenenwenenwneneseswnewnenene
nwwsenwnwnenwnenwnenwneneneenwnwsenenww
wwwsewwnwwwnewwneswwewww
swseswwswseswswswswsenwseneeneewsenwsw
nwnesenenwenwnwnwnenwnwnwneswnwnwnenene
seeeweswnenenwsenewenenwewneseee
nwwnwneseswsesweenweswsese
seeseseswsesenesesesenesewseseseeese
swwswneswwnwswneswwewsesewswswsww
seswneswswseswswseseswnwswswswswseswew
wwwwwswwewseswwwwwswwnenesw
nwnwwsenwnenwnwnwnwneenwnwnwnwnenwnww
nwnwneswwswseswswnwnwenwnenesenenenwswenw
neneneneeneeseneneneeneneneswnwnenee
neeeswswnweenwsweseneeseswnwnewe
neswesenwneneneenenweeneene
swseeneewnwseeeenwesenweseseeswnw
eweneeneseeneneneneeeseeeneewene
eeneneewneneeeswneneeneeenwsenenew
nwnwswsweswswnenwswseswswswsweswswnesw
neeeeseeeswewenenwswnene
nwenwnwenwswnwnwwnwswnwnwneswnwneswswese
neswseweeneneeeseenwwnenesenenwnee
wswwseewwwewweewwswnewwwsww
swswswwswswwwswswswswswnweeswswswsw
enenenenenenenenenenwnenenwsenenenewnw
seseswseseseeswseneseseseseseneseesee
neewneeweeeeeneese
enewneseeweneneeneneewenesenene
enwswneeswnwswsewenwwnesewneswseswe
senwswnwnenwnwwnenwnwswnwnwnwnwnwnwnwnwe
sewswneswswswseseseseswswseneswseswswsw
nwnenwwsewneneswnweenwnwnenwnwnwsenene
eswwewswswnwswsw
wwwwwwwwswsenw
nwnwnwnwnwnwnwwwnwnwwnwnwwnwnenwsese
seswnewnenwnweswnwsesenwseeseesesewnw
neneseneeswneneneswwsenwnw
nwnwnwnewnwnesenwnwnenwnwswnwneseenwnw
wwneneeneswneneeewwnesesenenenese
eseeswswsesenwneeewswnenwnwnewnw
nwnesesenewwwswnwewsenwwsewnwwww
eneeenewneneeneneneneswnenwewnesee
neneenewenenenenew
nwsenweewnwwwwenwnwswnwnenwswnwnwse
seseeeeeeswwsenwseeseeseseeese
wwwnwwwwwwwewewwwwwww
swswseseneseswswsewseseseswenwneseseswsw
seswsesesenweseeseswwseseneswsesesesese
swswseswswswswswswswswswnwswswseswsw
nweeneewneeseseesenwsenwseweswnwnw
eeeeeseseeeeewsweenweeeese
nwesesesesenenewwwneeeeweeee
eenenwneneeswewneeeeneenee
seseseswseswseswsenwseeswsesenwseseswne
eseseseswseeneseeseseewnwswsesenese
nwnenwnwseewsenwenewsenwsweswswenenee
wsenwnwwnwwnwneeenwnwne
seswswswswseneneseseswswswswswswswwnesww
wswseswnwsweswseseswesesenwswseseseswsw
sewweseseneseneswsesesenesesesesesese
nwwnwneewwewwwwnwwwwwswwwswsw
nwsweswwneeeeeenwseeenwnwswswesw
wwwwwwsenwwnewwnwwwenwwwew
swneneneswneneswenenwnwnewnwnwsenenenwnene
eswnweseweseeseenwsene
esewewneneneneseneneneneneneneneewwne
eneeeenesenwnenwseneneenenenweesw
nwnwnwseenwnweswnwnwnwnenewnwnwnwswenw
neenenesewsewneeswseseenwweeeesw
eewneeeneeesweeeeeeenenee
nenenenenenwwsenenenenenenenwswneneneene
nwwwwswwwnewwwwwwnwwww
enwswseswenesenwenwseseeswesesenewse
swesweneeenwenenweeneneesweeee
wnwnwnesenwnwwsenewswnwwnwsenwseneswse
neseswseneenwsweneswwnwsenwnesewsenwsw
swswswseseneswweenwswswsesenewseswnesenw
weseseeseseswseseseneeeesesewnese
seeneswnewsesewnwwwwnw
sewseeseeeeesewneeese
seseseenwewsesewneseeeeesweenw
ewswwwswswwswwwswswswsw
nwnwwwsenewswnwwwenwsenwnenwnwnwnw
esenwseseweeneneneswwsewsesewneese
wnwnwswnenwnewwenenesewnenenwnesenesene
wnwnenwwnwnwnwnwnwnwswnwnwnwnwwnenwnwse
eewnesenwsesesweeneeewesweeesee
swenwesweseenwseeseseseenenwesee
nwnwneswnwenwwnwnwnenenwnwnweneswsenw
swwwewwnewseewswwswnewwwww
swwwswewwwsewwsewnwwswwwwnww
wsenwewnwwsewwwnwsewnwnwwsenwnwnw
neswswnenenwneneneenewneneneswnwsw
wwwswwwwnwewwwsewwwwwwwnw
seseseswseswswnweswwswswswnwsesesesesee
nwneneenesenenenwwnwneneswnwnwnenenenwnw
neeenwneeneesweenweeeesw
eweeeeeeeeeeeeneswneeeswe
wseewesesesesesesesesewseenesesesesee
eeeeeseeeeweeee
wsewneseeewseswnewnenenwnenewnesenw
wswenwnwnwnwwnwnwnwwewnwwnwwnww
wwwwwwnewwwsewwwswwneseww
wwwwewwwwwwnw
nwnwnenenwnwnwseenwwsenwenwnwwwnw
seeswswsewnewnwwsweswwswnwswswnwnw
eweseseneeseese
sweeeeeswenenesweseeeeseneee
wnwswewnenewsewwnewwwswwsww
nweenwwwneswnwsenwsewewnwwnwnwww
eswneeneneneneeeneeneeneneeeswne
eeseseneeeeeeeweeneeeswee
enweeseneswnenwnwnwswswswnw
swseseseseseeseeneeese
swswswswswswswswwseswswswswswseeneswnwsesw
senwseenwwsweswseseswse
wnwwnwwnwnwnwwsenwnwnwnewnwnwnwsenwnwse
seseenwesesenwseseseseseseseseseseswswsw
nesewnenenwnwneneswneneswsenwnenwnenw
eswnwweenweseeneeswneeeeeee
seesweneewenenweswseseweseneswsenwse
wsesesesenesesesesesesesesesesese
neneneneenenenenenewneneneneneneswne
eseseeseeseeenweeeswseesenwse
neneseeeeweseewwseseeenweseee
senewnwwwswwewnwwnwwsewenewse
seseseeweseseseneseeeseweseseseee
wswseswseenwwswneswswnwswsww
nwnwnwnwwswnwnwnwnwenenwenwnwnwnwne
sewnwsenweswswswneenwwsenewnwnewnwnw
swseeseseswseneswwsesewwwswnenesesese
eeeneneesweeeeeeneee
nwnweswnwnwenwnwnwnwnwswnwsenwnwnwsenw
swswswswnwenwswswswswweswswesw
nenwnwneswnwneswnenwnenenenwnwnenenenene
wneneneneneneneneseswneneesenewnenwe
enwsenenweneeswswsesesweseseseseswsese
swwseseseeseewnesewnewswseseswseswse
enwneeneneswneneneenenenene
eswweeeeseeneeeeeesesenweee
nenwsenwnwnenwneswnwnwnwnwenwnwnenwnenw
esenwswwnwnwenwsenwnwseseenwswnwwew
nwswnewwwnwswnwwnenwnenwswnwwwwnwnw
eeweseeseseeeeeeesesesewese
nwseeeeenwseeseeeeseeeseeeew
senenwswnweswnwwwwwnwnenwwseswwnwe
ewswnwnewewsenwswseneswswswswseswsw
nwseswnenwwenwwswsesenwnwneewwnwse
seeneseseneweseseseeseseswseseseese
wwsewwswswwswswneswweswswswswwsww
swswswsweswswswswswnwwswswsesesweswsw
seeeeweweeweeeseneenewene
nwseseesewseesewnwneewseesesenenwee
swewwnwnwswswwwweswswswswswneswe
eeneeeneneneneeweneneenesenenenew
swsewwwsewnewwwnwwwwwwnewww
seneswwweswswswwsweswswswswswwswswwnw
seneseseseswsesesewsesesesesw
seswswseswswwewswswswswseswswswswnenw
eseseseesesenenweseesweseeewseseese
swesenenwswnesesenwwwnwse
nenewswnenenenenenesenenenenenenenenesw
senwneseneeneenenw
wseseseeseseeseseseeseseseeenesewe
neeeneweenenee
nwsenenwnenwneeneeeneneneneeswnesene
nwswseeneseenwswnweseneswswnweesesese
nwseseseswsesesesewseeesesesese
eswenesewnenwnwwwnwnwnwneswesenwswsene
sewswwswwswswwswwswswwwneneswnwsww
nenwswenenenenesesesenwwneswnenenewew
senenwswseswsewwsewseseseneeswneswswsw
nwwwnwswswseswseswswwnwweswwwew
eswswswswseseseswswseswswnwswsweswwswse
nenesenenewnenenwnenenenesenenenenenenesw
wnwnwnwwwwwewwwswwwnewnwsenwsw
enwnewnwneswewnewwswwneeseswesew
nwnwnenenwsenwewnenwnenenenwnenwnwnwnwsw
nesenewneenwnwnwnwnwneneneswneswnewnee
ewenewswwsewenwwsenenwwswnwsenwnw
nesenwsenwseseeswswnwese
wnwsenwnwsenwnwswwnwwnenwnwseswnwnwne
newnenwneneenwesenesenenwseseweswswe
senwsesesenwsweseswswsenwnesesesww
sweswseswswwseseseswswsesesenwneseseswnw
nwwenwnwnwsenwnweswnwswnwwswnwnwnenw
enesenenwsewesewsweeneeeeweeee
nwnwnwnwwnwnwnwnwnwwwewnwenwnwnwnw
wseswseseswneeseeseenwseenwseswnwse
seesenwnwwwewseswswnwnwnwe
sewwwwwwwweswwswwwwnewww
neneeswnenwneneswsenweneswneseswseeww
nwnwswenwnwnwnwnwneseswnwsweneswenwnwsw
wwwswwneswwwwwnewswww
senwnwnenwenenenenwnwnewswnwnwnwesw
wswwwwnwswwswwewswnweswswwswew
swseseseswseseswswseseswsesesesenesenwse
nwwnenenenwswsweneenenenenesweneeene
wwnwswwswwswewwwsewwwswswswe
ewwnwwnenesweseenwswswseeswwneenww
eseswsesenwwnwseseseseseseseseswesesesw
wwwwwsewwwwnenwsewnwnenwwwww
nenenenwneneeneswnenenenenwwnenwneenw
seeeeeeeswwseeeeeweneeeenw
senweeneeneswwneeneesweeeswenenesw
nwwnenwnwnwenwnenwnwnwswswnwnwnwenwse
sesenwseseseeseseseseseseese
swswneswsewseseswseswseswseswseeswsewse
seseeseseseeeesesesesewee
seneneeswnenenenenenenenwsenwnenenwnenenew
eeeneeneneweeewneeneneneeseene
swneneneneeneneneenenenenwneenewnene
seswnwseswnwnewneswswnesenewswwwswswsw
enweseeweewewesweeenw
wwwswewneswwwsesewwwnwwswswww
nwwwswwneswwsewswse
swwneseswswnewwswnewwwwse
nwwnwwwnwewwnwswwwwnwwnwwewnw
seseseswneseswseeseswswseswseswwesesenwsw
nweseseseseseseswewseseswsesesesesesese
seseswesesenwseenwsenwseseseseseseseswse
swsenwwnwnwnwnwneswewnenwnweweeswne
eeeenweeeweeeeeeeeesee
nwwwwswnewswewwenwnwwwewswwnw
nwnwnwnwwnwswenwnwnwnwnwnwnwnwnwnwnw
nwwsewewnesewswewnwswwnwwneewse
wnwnwwnwwwnwwnwnewwswwswwwne
enenesweeeeeeneenweeneeneeesw
neeeenweneeneneneneeeeeswsweee
sweswwewseswwwseneneswsewnwwsww
neesesenweweseneseeesesewseeseenwe
sweeeneeeswnene
nwwwswwnwseeweswwwnw
ewswswswwwwneswswnwswswwswswswwww
neewseenwneeswseeneweneweenwesw
seneweseeseseseewseseswweeeese
eneswswswnwswwwswswswswswswswswneswsw
sewswswswswnwswseswswswswnewswwwsww
wwsesenenwnewwwsenw
swnewweswwenenwneseenenenenenenewne
nwwnwnwnwswnwnenwwwnwnwnw
sesesesenwseswnwseseseseseeseswswswswse
swnwswenenwswswneweswwsewsw
nwnwnwnwnenenewewnenenenesenwnwswnwnw
seseswsewswswsenwseseesesenenwesenesww
neneeneeseeeewwwneeenweeeswe
enenwewwswswsenewswsenwewseeneenee
nwwenwswwwnwwnwnwwnwwwwewenwww
sweswnwswesenwsweswseswswnwnwswsweswnwsw
seseseneseseweseewseseswsesewsesese
eweneeneeeeeeseeeeeeeeesw
ewwwnwwwwswwwswswwwwwswwnesw
swnwnenwnwnwwnwnewnwswnwenwnwnwsenwnw
swneeswseseneswwnesesenwsesesenwswnww
seswneseseesesewseseene
wnwwsewnenwnwwsesesenwnwsesesewwwne
eswswwwswseswewwswwswnwswswwwnw
enwnwnenenwnwnwswnwnenwnenwnwswnwnw
newsesenwnenenwnwenwnewnwwnwnwswnwnwnwnw
swneneenesenwwsenwnewnesesenenenwnenw
neneenwnwswswswweeeeeeeenenee
swswseswnwswswswenwswsesenwswseswnewswse
newnenwnenewsenewnesenewneesenwnene
neseseseseswsesewseswneseseswsesesesese
ewseeeeseeesesesesenwseeeswse
wseeeseeeseseesewseenwswseneeee
neseneseswswsesenesewswsesenewsesesenwse
swneneneneneenwneeswneneneeneneneswne
eenewnenenesweeenenenenene
nenenesenenenwneeneeneewseeeene
nwsenenwnenewnwnwnwnwnwnenwnenwnwsenenenw
swnwenwnwwnwnwnwswswewnwnwnwnenwnwnwnww
wwswnwwewwwwsewnwwwww
wseseswnenewwwwwswwwsw
swswwswswwnewswwwseeswwwswwswsw
enesesewewsesweeeseeseseseseesese
nwwnewenwnenwnwnweneswnwneswnenwneenw
eweeeeeseeeweweneeeesesese
wswswswswswswnwseswneswswswswwwswsww
swsenwnwwnwseseseswweeneenwnesenwnee
neeswneneneneewneneneneneneneneneene
nwnewnwnwnwwnwnenwwswnwnwnwwsenwsenwnenw
nwnwnwnwnwnwnwnwsenwnwnwnw
nwnewnwswwwswneewsewnewwswwwww
eeswwesesesenwseeeeeeseeenwe
nenwneswswenwsweneeswneneneneneeswnenw
neneseeneneesewneswnenenwnw
nwnwwwenwenwnwnwwnwnwnwnwwnwswnwnwnw
seseseswswseswsenwswnenwseswwweseswnese
wwewwwseswwswsenwwnwweswnwnee
neenwnwseeneewwneneenenenesewseenese
nwwswswenesewwwwswwswenwneswnewse
seswwnenwnwnenwwneeswsewewsewsesw
eseeseseeeesweneee
eenesesweeeeenwswnwneenenwswnenene
seneseseeeseeswswseswsenwsenwnwsesesese
seseseseseeeeseseeenw
wnwwwweewwwwwswnewwswwww
swswnewnwswseswswswswswwwswswswswwsw
nwnwenwnwnwnwewnwnwnwnwnwnwnwswnwnwnw
seswswswseseseswseswswnwneseneswswseswne
swseswseswswswsewseswsesenenwsesenwseseese
swswsweseswneneswwnewswswswswswswswnew
nwwnwnwnwswnwnwnwnwsenwnwneeeswnwnwnenw
wneneneneseneneew
weeeseweneenewseesesewesesesese
swnweswswseeseswswswseswswswswnwseswew
eneseenweeeswneeeenweswneeee
neneenewneweneneeneseneneswneenenwnene
nesenewneneneeseswneneeneenenwenewnw
neneneweeneneewneeneeneneneene
senenewnesewwwwswswneswwneswsenwse
eenweneseeswnenweswnwsee
nwnwnwsenwnwnwnenwneneneswnwew
sweswneseenwesweeswnwewseneneneeenw
swnwneswwswseswswswswseswseseswswsesw
nwnwnwnwnewnwnwnwsewewsenw
swseseseseswseswswswsenwse
nenwnwesenwnwsenwwnwsenwneswneeneswnw
ewwwewnwwsewnw
nwwnwwnwnwswwnwnwnwnwwnenw
wneeneneneenwswswwneneeneneenesene
nenwnenwnenwnwnenwnwneesenwnenenenwwnew
eenewnenwswwseeenwsenwweneneswne
nwnwnenenwnwwnwnwnwnwswnwswsenw
eeseneenenenenwwseswneneewneenenenee
nenwnenewnwswnenewnwseswneenwnenesene
wnwswwnwwenwenwnwwnwswnwnwnwnwnwnww
neeneneenesewneseenenewnwenwswenese
nwewneeswnwnwseseneswneneswnenwswnwnw
nwnesesewseswsewsewnenenesesenewsesese
seneseswswswswswsenwseseseswseswswswsee
nwwswnwsewwwnewsewnwewesewnwnwnw
eswwenwnenwnwnenwswnwnwnwnwsenenwwne
senweesenwwsewseeneeeenesewseee
nenwnenwnwnwswnwswnenwnenweeswnenwnenene
wnwnwwewsewnewwswwwnwnwwnwwwww
nwwnwswnwnwwnwnenwnwswseewnwnwnwnwe
nenwnenenenwnwnwnenwnenenweenenenwwnesw
wnwnenweseneswwswnwneeseswnenenwswwe
eeeweeeeeeweeeseeee
wwwswwnwwnweswweneswnenwwwnwww
swswwswswseswswswsweseswswseneswswse
seswnwewswwwwswwsewnwneswswewww
seswwwwnewwnwwewwnewwwwww
seneswnenwsweewnwnwenwswswswnesenew
eswnweeesweeseneeeeeeeeeee
wnwswswswswwswswswswwswwwewewsww
nwnwnenwnwnweeswsenweesewswswnwnwswnw
seswwnwsewwwwswsenenw
wwswwwwswswseswwwwewswwswnww
seswseseswseseswseseseswswseseswswnw
swnesewwnwwneswne
wswswsesweswswswseswwswswsweswswnwnwe
seenwsenweseseseesesewseseseseesese
esenwnwnwneswnwnenwwsenwnenwwsenenww
eeeeeneseswseseeseenwseeesw
swseseeneseneseeswwnwese
eeeenweswseeeesee
seseswweenwswnewwwwnew
wswswswnwswswwswswswseneneswseseseeswse
nwswwnwsewewswwswwwenenwwnwww
seneseweseseeneesesesesesenweseseswse
nwnenwnwnwnwsewwenwnenwsenesenwnwnenwne
senwenewsesesewnwwseeweseswsesesenwe
wenwewnwnwnwwnwewnwwwnwwwwnw
seeeeseseeseseesenwseenweesesese
swswswwnwswwwwswnewswswwwswswwew
nenwnenenwnwnwsenenwneneneswnwnwnwsesene
wnewswsenesewswwwswnwwswswnewwseew
wsesenwenwseswsenwwseeseenesenenwwnw
senewewswwswwewwwwnewswwwswsw
swneenwseweseeenwweseseeesenwnwse"""


lines=input1.split('\n')
tiles=defaultdict(lambda:False)# false = white

def get_neighbours(x,y):
    yield x+1,y+1
    yield x+1,y-1
    yield x-1,y+1
    yield x-1,y-1
    yield x+2,y
    yield x-2,y

def day():
    global tiles
    tiles2=defaultdict(lambda:False)
    for x,y in list(tiles.keys()):
        black_tiles=sum(tiles[nx,ny] for nx,ny in get_neighbours(x,y))
        if tiles[x,y]: # black
            if  black_tiles==1 or black_tiles==2:
                tiles2[x,y]=True
        else:
            if black_tiles==2:
                tiles2[x,y]=True
        
        # calculate for neighbour tiles too because all tiles needs to be covered
        for x,y in get_neighbours(x,y):
            black_tiles=sum(tiles[nx,ny] for nx,ny in get_neighbours(x,y))
            if tiles[x,y]: # black
                if black_tiles==1 or black_tiles==2:
                    tiles2[x,y]=True
            else:
                if black_tiles==2:
                    tiles2[x,y]=True
        
    return tiles2
    
#main
for l in lines:
    # find directions in order
    directions=re.findall('(se|sw|ne|nw|e|w)',l)
    
    x=y=0
    for d in directions:
        if d=='se':
            x+=1
            y+=1
        elif d=='sw':
            x-=1
            y+=1
        elif d=='ne':
            x+=1
            y-=1
        elif d=='nw':
            x-=1
            y-=1
        elif d=='e':
            x+=2
        elif d=='w':
            x-=2
        
    tiles[x,y]=not tiles[x,y]

count=0
for t in tiles.values():
    if t:
        count+=1

print('a)',count)

for _ in range(100):
    tiles=day()
    
count=0
for t in tiles.values():
    if t:
        count+=1
print('b)', count)