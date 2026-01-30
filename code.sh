#!/bin/bash

ASCII_ART='
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
'

WHITE="\033[97m"
GRAY="\033[37m"
RESET="\033[0m"

COLORS=(
  "\033[31m"
  "\033[32m"
  "\033[33m"
  "\033[34m"
  "\033[35m"
  "\033[36m"
  "\033[91m"
  "\033[92m"
  "\033[93m"
  "\033[94m"
)

cleanup() {
  echo -e "${RESET}"
  tput sgr0
  clear
  exit 0
}

trap cleanup INT TERM

while true; do
  for COLOR in "${COLORS[@]}"; do
    clear
    echo -e "${WHITE}"
    echo -e "${COLOR}${ASCII_ART}"
    echo -e "${GRAY}\nHacked By Eloy P. (e0x)${RESET}"
    sleep 0.5
  done
done
