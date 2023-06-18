import Navbar from "@/components/navbar";
import RecipeList from "@/components/recipelist";
import { urbanist } from "./_app";

export default function Recipes() {
    return(
        <main
            className="
            bg-pale-green 
            min-h-screen 
            font-sans"
        >
        <div className={urbanist.className}>
          <Navbar />
          <RecipeList />
        </div>
      </main>
    )
}