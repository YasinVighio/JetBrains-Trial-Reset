rm -rf ~/.config/JetBrains/PyCharm*/eval
sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/PyCharm*/options/other.xml
rm -rf ~/.java/.userPrefs/jetbrains/pycharm

rm -rf ~/.config/JetBrains/IntelliJIdea*/eval
sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/IntelliJIdea*/options/other.xml
rm -rf ~/.java/.userPrefs/jetbrains/idea

rm -rf ~/.config/JetBrains/WebStorm*/eval
sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/WebStorm*/options/other.xml
rm -rf ~/.java/.userPrefs/jetbrains/webstorm

rm -rf ~/.config/JetBrains/PhpStorm*/eval
sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/PhpStorm*/options/other.xml
rm -rf ~/.java/.userPrefs/jetbrains/phpstorm