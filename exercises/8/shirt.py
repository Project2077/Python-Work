# 练习8-3：T恤 　编写一个名为make_shirt() 的函数，它接受一个尺码以及
# 要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
def make_shirt(size="Large", message="I love Python"):
    """概要地说明T恤的尺码和字样"""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')
# 使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。


make_shirt("Large", "Hello")
make_shirt(size="Small", message="Nice")

# 练习8-4：大号T恤 　修改函数make_shirt() ，使其在默认情况下制作一件
# 印有“I love Python”字样的大号T恤。调用这个函数来制作：一件印有默认
# 字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤
# （尺码无关紧要）。
make_shirt("medium")

