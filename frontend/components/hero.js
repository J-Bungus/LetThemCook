import Image from 'next/legacy/image'
import hero from "../public/hero.png"
import { Flex } from '@chakra-ui/react'
import ButtonUnit from './button'
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';
import SearchBar from './searchbar';
import Ingredients from '../../backend/ingredients.json';

function Hero() {
    return (
        <Flex direction="column" gap="10">
            <Flex align="center" justify="center">
                <div>
                    <h1 className="text-5xl p-10">What are we cooking with today?</h1>
                </div>
                <div className="w-2/4">
                    <Image 
                        src={hero} 
                    />
                </div>
            </Flex>
            <Flex justify="center" gap="20">
                <SearchBar data={Ingredients}/>
                <ButtonUnit padding="px-16 py-12" url="/recipes" icon={<FormatListBulletedIcon/> } name="Recipes" size="lg"/>
            </Flex>
        </Flex>
    )
}

export default Hero