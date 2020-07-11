import Head from "next/head";
import Favourites from "../components/cookbook/Favourites";
import Owned from "../components/cookbook/Owned";

import { useSelector } from 'react-redux';
import RecipeIcon from "../components/cookbook/RecipeIcon";

export default function CookBook() {
  
  return (
    <>
      <Head>
        <title>Pantry Pirate | Cookbook</title>
      </Head>
      <div>
        <Favourites/>
        <hr/>
        <Owned/>
      </div>
    </>
  );
}
