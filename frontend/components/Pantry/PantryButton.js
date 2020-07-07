import styles from "./Pantry.module.scss";

import React from "react";

import Pantry from "./Pantry";

export default class Indicator extends React.Component {
  render() {
    const playHoverPop = () => {
      let audio = document.getElementById(`pop1`);
      audio.play();
    }
    return (
      <>
        <div
          onMouseEnter={playHoverPop}
          onClick={() => document.getElementById("pantry").classList.toggle(styles.pantryShow)}
          className={styles.pantryButton}
        >
          <img src="/fridge.svg" />
        </div>
        <Pantry />
        <audio id={`pop1`}>
          <source src={`/audio/pop1.mp3`} />
        </audio>
      </>
    );
  }
}
