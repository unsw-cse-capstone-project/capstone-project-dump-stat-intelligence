import styles from "./Pantry.module.scss";

import React from "react";

import Pantry from "./Pantry";

export default class Indicator extends React.Component {
  render() {
    return (
      <>
        <div
          onClick={() => document.getElementById("pantry").classList.toggle(styles.pantryShow)}
          className={styles.pantryButton}
        >
          <img src="/fridge.svg" />
        </div>
        <Pantry />
      </>
    );
  }
}
