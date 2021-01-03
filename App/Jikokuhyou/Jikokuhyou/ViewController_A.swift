//
//  ViewController.swift
//  Jikokuhyou
//
//  Created by K K on 2021/01/02.
//

import UIKit

class ViewController_A: UIViewController{
    @IBOutlet weak var picker_Par: UIPickerView!
    @IBOutlet weak var picker_Arr: UIPickerView!
    
    @IBAction func myUnwindAction(for unwindSegue: UIStoryboardSegue, towardsViewController subsequentVC: UIViewController) {
    }

    let dataList = ["泉西", "高池前", "上田4", "盛岡駅"]
     
        override func viewDidLoad() {
            super.viewDidLoad()
            picker_Par.dataSource = self
            picker_Par.delegate = self
            picker_Par.tag = 1
            picker_Arr.dataSource = self
            picker_Arr.delegate = self
            picker_Arr.tag = 2
        }
    
   
   
}

let Par_list = ["泉西", "高池前", "上田4", "盛岡駅"]
let Arr_list = ["泉西", "高池前", "上田4", "盛岡駅"]

extension ViewController_A: UIPickerViewDataSource{
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if pickerView.tag == 1{
            return Par_list.count
        } else if pickerView.tag == 2{
            return Arr_list.count
        } else {
            return 0
        }
    }
}


extension ViewController_A: UIPickerViewDelegate{
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if pickerView.tag == 1{
            return Par_list[row]
        } else if pickerView.tag == 2{
            return Arr_list[row]
        } else {
            return "None"
        }
    }
}

