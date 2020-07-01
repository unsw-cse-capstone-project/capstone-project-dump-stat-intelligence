import Head from "next/head";

import { useSelector } from 'react-redux'; 
import RecipeCard from "../components/RecipeCard/RecipeCard";

export default function Home() {
  const recipes = useSelector(state => state.recipes.recipes);
  return (
    <>
      <Head>
        <title>Pantry Pirate | Explore</title>
      </Head>
      <div>
        <br />
        <h1 className="title is-2">Explore Recipes</h1>
        <div className="columns is-multiline">
          {recipes.map((recipe, idx) => (
            <div key={idx} className="column is-3">
              <RecipeCard
                className="column is-3"
                src={`https://source.unsplash.com/400x300/?food&sig=${recipe}`}
                title={recipe}
                id={idx} // TODO: alter
              />
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
