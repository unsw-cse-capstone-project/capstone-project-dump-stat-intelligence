import Head from "next/head";

import { useSelector } from 'react-redux';
import RecipeIcon from "../components/cookbook/RecipeIcon";

export default function CookBook() {
  const favourites = useSelector((state) => state.recipes.recipes)
  return (
    <>
      <Head>
        <title>Pantry Pirate | Cookbook</title>
      </Head>
      <div>
        <br/>
        <h1 className="title is-3">My Favourited recipes</h1>
        <div className="columns is-multiline">
          {favourites.map((recipe, idx) => (
            <div key={idx} className="column is-3">
              <RecipeIcon fave={true} title={recipe.name} id={recipe.id} src={`https://source.unsplash.com/400x300/?food&sig=${recipe.id}`}/>
            </div>
          ))}
        </div>
        <br/><br/>
        <h1 className="title is-3">My recipes</h1>
        <div className="columns is-multiline">
          {favourites.map((recipe, idx) => (
            <div key={idx} className="column is-3">
              <RecipeIcon title={recipe.name} id={recipe.id} src={`https://source.unsplash.com/400x300/?food&sig=${recipe.id}`}/>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
