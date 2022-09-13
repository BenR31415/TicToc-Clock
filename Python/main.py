# import gpio_controls
import carousel

carouselObj = carousel.Carousel()

if __name__ == "__main__":
    for i in range(0, 31):
        carouselObj.addBiscuit("1111")
        print(carouselObj.slotsUsed)
        carouselObj.dispense(3)
        print(carouselObj.slots)
        print(carouselObj.hasSpace())