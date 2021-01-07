//
//  ViewController_B.swift
//  Jikokuhyou
//
//  Created by K K on 2021/01/02.
//

import UIKit

class ViewController_B: UIViewController {
    
    var imageName : String!
    @IBOutlet weak var pickLabel: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        pickLabel.text = imageName

        // Do any additional setup after loading the view.
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
