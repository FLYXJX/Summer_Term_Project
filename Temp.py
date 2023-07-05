class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hands = []

    def add_hand(self, hand):
        self.hands.append(hand)

    def cout(self):
        print("姓名：{}，年龄：{}".format(self.name, self.age))
        for hand in self.hands:
            for finger in hand.fingers:
                print("手：{}，手指：{}".format(hand.name, finger.name))
                for landmark in finger.landmarks:
                    print("X:{}\tY:{}".format(*landmark))


class Hand:
    def __init__(self, name):
        self.name = name
        self.fingers = []

    def add_finger(self, finger):
        self.fingers.append(finger)


class Finger:
    def __init__(self, name):
        self.name = name
        self.landmarks = []

    def add_landmark(self, landmark):
        self.landmarks.append(landmark)


# 示例用法
a = Person("小明", 10)

hand1 = Hand("左手")
finger1 = Finger("食指")
finger1.add_landmark([10, 20])
finger1.add_landmark([30, 40])

finger2 = Finger("中指")
finger2.add_landmark([50, 60])
finger2.add_landmark([70, 80])

hand1.add_finger(finger1)
hand1.add_finger(finger2)

hand2 = Hand("右手")
finger3 = Finger("拇指")
finger3.add_landmark([90, 100])
finger3.add_landmark([110, 120])

hand2.add_finger(finger3)

a.add_hand(hand1)
a.add_hand(hand2)

import json

people = [a, a]
data_list = []
for person in people:
    data = {
        "name": person.name,
        "age": person.age,
        "hands": []
    }

    for hand in person.hands:
        hand_data = {
            "name": hand.name,
            "fingers": []
        }
        for finger in hand.fingers:
            finger_data = {
                "name": finger.name,
                "landmarks": finger.landmarks
            }
            hand_data["fingers"].append(finger_data)

        data["hands"].append(hand_data)
    print(data)
    data_list.append(data)
# # 保存为 JSON 文件
# filename = "xiaoming.json"
# with open(filename, "w") as file:
#     json.dump(data_list, file)

# print(f"小明的数据已保存到 {filename} 文件中。")
