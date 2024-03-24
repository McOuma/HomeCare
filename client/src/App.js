import React, { Component } from 'react'
import Footer from './components/layouts/Footer'
import Landing from './components/layouts/Landing'
import Navbar from './components/layouts/Navbar'


export default class App extends Component {
  render() {
    return (
      <div>
        <Navbar />
        <br/>
        <Landing />
        <br/>
        <Footer/>
      </div>
    )
  }
}
