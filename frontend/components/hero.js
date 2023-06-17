import Image from 'next/legacy/image'
import hero from "../public/hero.png"
import { Flex } from '@chakra-ui/react'
import ButtonUnit from './button'
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';
import RestaurantMenuIcon from '@mui/icons-material/RestaurantMenu';

function Hero() {
    return (
        <Flex align="center" justify="space-around" gap="10">
            <div>
                <Flex direction="column">
                    <h1 className="text-5xl p-20">What are we starting with today?</h1>
                    <Flex justify="center" gap="10">
                        <ButtonUnit icon={<RestaurantMenuIcon/> } name="Ingredients" size="lg"/>
                        <ButtonUnit icon={<FormatListBulletedIcon/> } name="Recipes" size="lg"/>
                    </Flex>
                </Flex>
            </div>
            <div className="w-2/4">
                <Image 
                    src={hero} 
                />
            </div>
        </Flex>
    )
}

export default Hero